class pali{
public static void main(String args[]){
int a=101;
int k=a;
int A=0;
for(int i=0;i<3;i++){
	int n=a%10;
	A=n+A*10;
	a=a/10;
}
if (A==k){
System.out.println("palindrom");}
else{
System.out.println("not a palindrom");}
}}