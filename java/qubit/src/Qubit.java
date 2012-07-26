import java.io.*;
import java.math.BigInteger;
import java.util.ArrayList;

/**
 * Created by remim
 * Date: 6/6/12
 * Time: 7:20 PM
 */
public class Qubit {

    public static String data1 = "/Users/remim/Documents/qubit/data1";
    //public static String data4 = "/Users/remim/Documents/qubit/data4";
    public static String data4 = "/home/saul/Downloads/qubi/data4";

    public static void main (String[] args) throws IOException {

        int n = 1000;
        //String[] set = constructDataSet(n,10,data1);
        //TreeNode root = createTree(set, n);
        //printTree(root, 0);
        //System.out.println(set[0]);
        //System.out.println(getMaxLen(set, n));

        //long l = 1131016214110;
        //BigInteger n1 = BigInteger.valueOf(1131016214110);

        //verifyCode1(data4);

        //assertBinary(root);

        soWhat();

                        /*
        for (int i=0; i<50; i++){
            System.out.println(set[i]);
        }                 */
        return;
    }

    public static void soWhat(){
        String line =  "0.86773414468182696879239301779307425113101621411075:0.13226585531817303120760698220692574931101930403025";
        /*
        0.86773414468182696879239301779307425113101621411075
        0.13226585531817303120760698220692574931101930403025
        */

        BigInteger i = new BigInteger("86773414468182696879239301779307425113101621411075");
        BigInteger j = new BigInteger("13226585531817303120760698220692574931101930403025");

        BigInteger[] k = i.divideAndRemainder(j);
        System.out.println(i.subtract(j));

        //01234
        //98765

        long l1 = 1131016214110L;

        // l1 + code1
        long l3 = 8868983785889L;

        // l2 + code2
        //01234
        //56789
        long l4 = 4866564859585L;


        long l2 = 9311019304030L;

        /*primeDecomp(l3);
        System.out.println(GCD(l1, l3));
//        primeDecomp(l2);

        System.out.println(Long.toString(l2,5));

        System.out.println(Long.toBinaryString(l2));
        System.out.println(Long.toBinaryString(l3));
        System.out.println(l3>>1);            */

   }

    public static void primeDecomp(long n){

        // for each potential factor i
        for (long i = 2; i*i <= n; i++) {

            // if i is a factor of N, repeatedly divide it out
            while (n % i == 0) {
                System.out.print(i + " ");
                n = n / i;
            }
        }

        // if biggest factor occurs only once, n > 1
        if (n > 1) System.out.println(n);
        else       System.out.println();
    }

    public static long GCD(long a, long b)
    {
        if (b==0) return a;
        return GCD(b,a%b);
    }

    public static boolean isPrime(long n) {
        boolean prime = true;
        for (long i = 3; i <= Math.sqrt(n); i += 2)
            if (n % i == 0) {
                prime = false;
                break;
            }
        if (( n%2 !=0 && prime && n > 2) || n == 2) {
            return true;
        } else {
            return false;
        }
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


    public static void verifyCode1(String filePath) throws IOException {
        File f = new File(filePath);
        FileInputStream fis = new FileInputStream(f);
        BufferedReader bf = new BufferedReader(new InputStreamReader(fis));

        char[] code1 = new char[10];
        code1[0] = '9';
        code1[1] = '8';
        code1[2] = '7';
        code1[3] = '6';
        code1[4] = '5';
        code1[5] = '4';
        code1[6] = '3';
        code1[7] = '2';
        code1[8] = '1';
        code1[9] = '0';

        String line;
        String separator = ":";
        String[] cut;
        long i = 1;
        int lengthElement;
        int lengthEnd;
        String end;
        String s0, s1;

        while (true) {

            line = bf.readLine();

            if (line == null){
                System.out.println("ok!");
                return;
            }

            cut = line.split(separator);

            s0 = cut[0].substring(2, cut[0].length()-1);
            s1 = cut[1].substring(2, cut[1].length() - 1);


            /*if (! respectCode1(s0, s1, code1)){
                System.out.println("Error : " + i);
                System.out.println(line);
                //return;
            } */

            if (s0.endsWith("7")){
                String subs = s0.substring(0, s0.length()-1);
                if ( ! (subs.endsWith("18") ||
                        subs.endsWith("68") ||
                        subs.endsWith("93") ||
                        subs.endsWith("43") ) ){
                    System.out.println("Error : " + i);
                    System.out.println(line);
                }
            }

            i++;

            //return;
        }

    }


    public static boolean respectCode1(String s0, String s1,  char[] code1){
        int length = s1.length();
        if (s0.length() != length){
            return false;
        }
        StringBuilder sNew = new StringBuilder(length);
        char c;
        int j;
        for (int i=0; i<length; i++){
            c = s0.charAt(i);
            j = Integer.parseInt(String.valueOf(c));
            sNew.append(code1[j]);
        }

        return (sNew.toString().compareTo(s1) == 0);
    }

}
