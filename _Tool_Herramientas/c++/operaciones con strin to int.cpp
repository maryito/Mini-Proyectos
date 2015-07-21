// Programas para realizar operaciones matematicas basicas de un digito automaticamentes

#include <iostream>
#include <cstdlib>
#include <string>
using namespace std;

int main(){
	string data;
	int valores[3]={};	
	float resultado;
	
	cout<<"Ingrese la datos: ";
	cin>>data;
	
	for(int i=0; i<data.size(); i++){
		char conversion = data[i];
		valores[i] = int(conversion)- int ('0');  // conversion de un  caracter a un entero 
	}	
	cout<<"Resultado ";
	for(int d=0; d<data.size(); d++){
		if (data[d]=='+'){
			cout<<"suma: "<<valores[d-1] + valores[d+1]<<endl;
		}
		else	if (data[d]=='-'){
			cout<<"resta: "<<valores[d-1] - valores[d+1]<<endl;
		}
		else	if (data[d]=='*'){
			cout<<"multiplicacion: "<<valores[d-1] * valores[d+1]<<endl;
		}
	}
		
	
	return 0;
}
