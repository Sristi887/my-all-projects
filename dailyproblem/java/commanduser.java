class user{
public static void main(String args[]){
int l=args.length;
if(l==0)
{System.out.println("novalue");}
else{
for(int i=0;i<l-1;i++){
System.out.print(args[i] +",");}System.out.print(args[l-1] +"!!!");
}}}
