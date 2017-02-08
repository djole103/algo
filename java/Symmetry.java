import java.util.*;

public class Symmetry {
  public static boolean isSymmetric(TreeNode root) {
      if(root == null) return true;
      Stack<TreeNode> ls = new Stack<TreeNode>();
      ls.push(root.left);
      Stack<TreeNode> rs = new Stack<TreeNode>();
      rs.push(root.right);
      while(!ls.empty() && !rs.empty()){
          TreeNode l = ls.pop();
          TreeNode r = rs.pop();
          if(l == null || r == null){
            if(r == l) continue;
            return false;
          } else{
              if(l.val == r.val){
                ls.push(l.left); ls.push(l.right);
                rs.push(r.right); rs.push(r.left);
              } else return false;
          }
      }
      return true;
  }

  public static void main(String[] args){
    TreeNode root = new TreeNode(1);
    root.left = new TreeNode(2);
    root.right = new TreeNode(2);
    root.right.right = new TreeNode(3);
    System.out.println(isSymmetric(root));
  }
}
