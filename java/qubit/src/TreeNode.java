import java.util.ArrayList;
import java.util.HashMap;

/**
 * Created by remim
 * Date: 6/6/12
 * Time: 10:14 PM
 */
public class TreeNode {

    private int value;
    private ArrayList<TreeNode> children;

    public TreeNode(int value){
        this.value = value;
        this.children = new ArrayList<TreeNode>();
    }

    public void addChild(TreeNode child){
        this.children.add(child);
    }

    public int getValue() {
        return this.value;
    }

    public ArrayList<TreeNode> getChildren(){
        return  this.children;
    }

    public TreeNode getChildren(int value){
        for (TreeNode child : children){
            if (child.getValue() == value) {return child;}
        }

        // TODO throw new ?
        return null;
    }

    public boolean hasChildren(int value){
        return getChildren(value)!=null;
    }
}
