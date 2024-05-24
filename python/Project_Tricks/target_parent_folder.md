# Target Parent Folder

    Sometimes you have a project and are troubleshooting a support module. 
    This is a trick to troubleshoot without having to run from main
    
## Example

    import os
    parent_dir = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
    path_to_target_from_parent = ['output','excel','target.xlsx']
    JenkinsReportObj.output_path = os.path.join(parent_dir, *path_to_target_from_parent)    # unpack target list