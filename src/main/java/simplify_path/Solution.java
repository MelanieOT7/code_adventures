package simplify_path;

import java.util.Stack;
public class Solution {
    public String simplifyPath(String path){
        String[] parts = path.split("/");
        Stack<String> stack = new Stack<>();

        for(String part : parts){
            if(part.isEmpty() || part.equals(".")){
                continue;
            }
            else if(part.equals("..")){
                if(!stack.isEmpty()){
                    stack.pop();
                }
            }
            else{
                stack.push(part);
            }
        }
        StringBuilder simplifiesPath = new StringBuilder();
        for( String part : stack ){
            simplifiesPath.append("/").append(part);
        }

        return simplifiesPath.isEmpty() ? "/" : simplifiesPath.toString();
    }

}
