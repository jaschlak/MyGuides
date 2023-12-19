# Split Array

    This splits an array of Strings into 2 seperate arrays of strings
    Inputs the array and character for splitting
    
    
## Main class calling:

        String[] ItemLabel = SplitStrings(Statement).Item1;
        String[] ItemValue = SplitStrings(Statement).Item2;
    
## Method:

        static Tuple<String[],String[]> SplitStrings(String[] list)
        {
            String[] ItemLabel = new String[] { };
            String[] ItemValue = new String[] { };

            for (int i = 0; i < list.Length; i++)
            {
                Array.Resize(ref ItemLabel, ItemLabel.Length + 1);
                Array.Resize(ref ItemValue, ItemLabel.Length + 1);

                String[] Temp = list[i].Split('=');
                ItemLabel[i] = Temp[0];
                ItemValue[i] = Temp[1];
            }

        return Tuple.Create(ItemLabel,ItemValue);
        }