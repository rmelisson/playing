import java.io.*;
import java.util.ArrayList;

/**
 * Created by remim
 * Date: 6/6/12
 * Time: 7:20 PM
 */
public class Qubit {

    public static String data1 = "/Users/remim/Documents/qubit/data1";
    public static String data4 = "/Users/remim/Documents/qubit/data4";

    public static void main (String[] args) throws IOException {

        int n = 1000;
        String[] set = constructDataSet(n,10,data1);
        TreeNode root = createTree(set, n);
        printTree(root, 0);
        //System.out.println(set[0]);
        //System.out.println(getMaxLen(set, n));

        //assertBinary(root);

                        /*
        for (int i=0; i<50; i++){
            System.out.println(set[i]);
        }                 */
        return;
    }

    public static void exp(String filePath, int max) throws IOException {

        File f = new File(filePath);
        FileInputStream fis = new FileInputStream(f);
        BufferedReader bf = new BufferedReader(new InputStreamReader(fis));


        String line;
        String separator = ":";
        String[] cut;
        int i = 1;
        int lengthElement;
        int lengthEnd;
        String end;

        // left or right element x:y
        int n = 1;

        while (true) {

            line = bf.readLine();

            cut = line.split(separator);

            lengthElement = cut[1].length();
            end = "75";
            lengthEnd = end.length();
            if (cut[0].endsWith(end)) {
                System.out.println(cut[0].substring(lengthElement - (lengthEnd + 1), lengthElement - lengthEnd));
            }

            //System.out.println(cut[n]);

            i++;
            if (i == max) {
                return;
            }

        }

    }

    public static String[] constructDataSet(int n, int wordSize, String filePath) throws IOException {
        File f = new File(filePath);
        FileInputStream fis = new FileInputStream(f);
        BufferedReader bf = new BufferedReader(new InputStreamReader(fis));

        String[] dataSet = new String[n];
        int i = 0;
        int length;
        int start;
        String separator = ":";
        String[] cut;
        String line;
        while (i<n) {
            line = bf.readLine();
            cut = line.split(separator);
            length = cut[0].length();
            if (wordSize == 0) {
                start = 2;
            } else {
                start = length - wordSize;
            }
            dataSet[i] = cut[0].substring(start, length);
            i++;
        }

        return dataSet;
    }

    public static TreeNode createTree(String[] dataSet, int n){
        TreeNode rootNode = new TreeNode(5);

        int length;
        for (int i=0; i<n; i++){
            //System.out.println("go " + dataSet[i]);
            length = dataSet[i].length();
            rootNode = iterate(rootNode, dataSet[i].substring(0, length-1));
        }

        return rootNode;
    }

    public static TreeNode iterate(TreeNode rootNode, String word){

        // we retrieve the last digit of the word
        int length = word.length();
        char lastDigit = word.charAt(length - 1);
        int value = Integer.parseInt(String.valueOf(lastDigit));

        TreeNode childNode = rootNode.getChildren(value);
        // if node doesn't already exist we create it and continue for the word - 1 char
        if (childNode == null){
            childNode = new TreeNode(value);
            rootNode.addChild(childNode);
        }

        if (length > 1){
            iterate(childNode, word.substring(0, length-1));
        }

        return rootNode;
    }


    public static void printTree(TreeNode rootNode, int i){
        for (int j=0; j<i; j++){
            System.out.print("\t");
        }
        System.out.print(rootNode.getValue() + "\n");

        for (TreeNode child : rootNode.getChildren()){
            printTree(child, ++i);
            i--;
        }
    }

    /*
    public static boolean assertBinary(TreeNode rootNode){
        if (rootNode.getChildren() == null) { return true; }
        if (rootNode.getChildren().size() == 2) {
            for (TreeNode child : rootNode.getChildren()){

            }
        }
    }*/


    public static ArrayList<String> getEndings(ArrayList<String> list){
        ArrayList<String> endings = new ArrayList<String>();

        return null;
    }

    /*

        ???? Do different trees exist btw left and right, data1 and data4? ????

        all elements can be represented as a path in a tree

        we need to create the tree

        one iteration :
            take n elements
                find a bunch of same endings (+ parents) shared by the n elements
                add these endings as children of to the parent
                iterate over all children with n

        read 10
        iterate(node(5), 10 data)
            finding 2 and 7
            create new node 25 and 75 with 5 as parent


     */

    public static int getMaxLen(String[] set, int n){
        int max = 0;
        int length;
        for (int i=0; i<n; i++){
            length = set[i].length();
            if (length>max){
                max = length;
            }
        }
        return max;
    }


}
