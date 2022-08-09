#include<stdio.h>

int main(){
int n;
int x[] = {1,2,3,4,2,1};
float y[20];
FILE *fp;

y[0] = x[0];
y[1] = -0.5*y[0]+x[1];

for(n=2;n<20;n++){
  if(n<6) y[n] = x[n]+x[n-2]-0.5*(y[n-1]);
  else if(n>5 && n<8) y[n] = -0.5*y[n-1]+x[n-2];
  else y[n] = -0.5*y[n-1];
}

fp = fopen("y(n).dat","w");
for(n=0;n<20;n++){ 
 fprintf(fp,"%lf\n",y[n]);
}   
fclose(fp);
return 0;
}
