# PS1 Prompt Structure

    How to test/modify the prompt for the user
    
    External Documentation: https://access.redhat.com/solutions/505983
    
## variables

    \u = username
    \h = hostname
    \W = current relative working directory
    \PWD = current absolute working directory
   
## prompt structures
   
    \u@\h \W\\$                                 # default prompt
    
    
## commands

    echo $PS1                                   # see current prompt structure
    PS1='<prompt_structure>'                    # modify current prompt Structure
    
## permanently modify prompt Structure

    1) open bash file
        a) vi /etc/bashrc                       # global change
        b) vi /home/<user>/.bashrc              # user change
    
    2) add the command to add the prompt Structure:
        PS1='<prompt_structure>'                    # modify current prompt Structure
        
    3) save, exit and restart your ssh session to see the change take effect
    
## Add this to your .bashrc to be able to see git status and color coding within your prompt structure:

    # get current branch in git repo
    function parse_git_branch() {
      BRANCH=`git branch 2> /dev/null | sed -e '/^[^*]/d' -e 's/* \(.*\)/\1/'`
      if [ ! "${BRANCH}" == "" ]
      then
        STAT=`parse_git_dirty`
        echo " ( ${BRANCH}${STAT} )"
      else
        echo ""
      fi
    }

    # get current status of git repo
    function parse_git_dirty {
      status=`git status 2>&1 | tee`
      dirty=`echo -n "${status}" 2> /dev/null | grep "modified:" &> /dev/null; echo "$?"`
      untracked=`echo -n "${status}" 2> /dev/null | grep "Untracked files" &> /dev/null; echo "$?"`
      ahead=`echo -n "${status}" 2> /dev/null | grep "Your branch is ahead of" &> /dev/null; echo "$?"`
      newfile=`echo -n "${status}" 2> /dev/null | grep "new file:" &> /dev/null; echo "$?"`
      renamed=`echo -n "${status}" 2> /dev/null | grep "renamed:" &> /dev/null; echo "$?"`
      deleted=`echo -n "${status}" 2> /dev/null | grep "deleted:" &> /dev/null; echo "$?"`
      bits=''
      if [ "${renamed}" == "0" ]; then
        bits=">${bits}"
      fi
      if [ "${ahead}" == "0" ]; then
        bits="*${bits}"
      fi
      if [ "${newfile}" == "0" ]; then
        bits="+${bits}"
      fi
      if [ "${untracked}" == "0" ]; then
        bits="?${bits}"
      fi
      if [ "${deleted}" == "0" ]; then
        bits="x${bits}"
      fi
      if [ "${dirty}" == "0" ]; then
        bits="!${bits}"
      fi
      if [ ! "${bits}" == "" ]; then
        echo " [ ${bits} ]"
      else
        echo ""
      fi
    }

    # Update prompt
    PS1="\[\033[0;35m\]\h\[\033[00m\]\[\033[1;33m\] |\[\033[00m\]\[\033[1;35m\] \u \[\033[00m\]\[\033[1;33m\]|\[\033[00m\]\[\033[1;36m\] \w\[\033[00m\]\[\033[1;33m\] branch\[\033[00m\]\[\033[0;36m\]\$(parse_git_branch)\[\033[00m\] > "
    PS2=" 🔪 "
    