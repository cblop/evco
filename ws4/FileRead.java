import java.io.*;

class FileRead 
{
 public static void main(String args[])
  {
    double aDouble = 0;
    double[] test;
    double[] target;
  try{
  // Open the file that is the first 
  // command line parameter
  FileInputStream fstream = new FileInputStream(args[0]);
  // Get the object of DataInputStream
  DataInputStream in = new DataInputStream(fstream);
  BufferedReader br = new BufferedReader(new InputStreamReader(in));
  String strLine;
  //Read File Line By Line
  while ((strLine = br.readLine()) != null)   {
  // Print the content on the console
  aDouble = Double.parseDouble(strLine);

  System.out.println (strLine);
  }
  //Close the input stream
  in.close();
    }catch (Exception e){//Catch exception if any
  System.err.println("Error: " + e.getMessage());
  }
  }
}



