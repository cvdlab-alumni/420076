//QUESTA FUNZIONE DEVE VISUALIZZARE IN FORMATO GRAFICO LO STANDARD .OBJ CONVERTENDO I VERTICI NELLA FORMA [a,b,c] ANCHE SE
//NON SI HANNO TALI ELEMENTI DISPONIBILI.


/*-------------------------------------------------------------
V Function

//Inizializzo la stringa come vuota
//Prendo direttamente il terzo elemento dell'array dei vertici, visto che dallo standard OBJ è richiesto di avere [a,b,c] invece di [a,b]
//Scorrendo l'array, se il valore "corrente" di z non è impostato, lo setto a 0
-------------------------------------------------------------*/
function vertici(origin){
	var string = '';

	for (var i=0; i<origin.length; i++){
		var currVal = origin[i][2];									
		if (currVal===""){												
			string+='v '+' '+origin[i][0]+' '+origin[i][1]+' '+origin[i][2]+'\n';
		}
		else{
			string+='v '+' '+origin[i][0]+' '+origin[i][1]+' 0 \n';
		}
	}
	return string;
}

/*-------------------------------------------------------------
FV Function

//Inizializzo la stringa come vuota
//Se durante l'iterazione si verifica la presenza di un solo elemento, stampo quello e termino l'intera funzione

-------------------------------------------------------------*/
function facciate(origin){
	var string = '';

	var lgt1 = origin.length;
	for(var i=0; i<lgt1; i++){
		var lgt2 = origin[i].length;
		for(var j=0; j<lgt2;j++){
			if(j == 0){string+='f '+origin[i][j]+' ';}					
			else{
				if(j == lgt2-1){string+=origin[i][j]+'\n';}					
				else{
					string+=origin[i][j]+' ';									
				}
			}
 		}
	}
	return string;
}


/*-------------------------------------------------------------
ESEMPI UTILIZZATI A LEZIONE PER FV,V
-------------------------------------------------------------*/
FV = [[5,6,7,8],
[0,5,8],
[0,4,5],
[1,2,4,5],
[2,3,5,6],
[0,8,7], [3,6,7], [1,2,3], [0,1,4]
]

V = [[0,6],
[0,0],
[3,0],
[6,0],
[0,3],
[3,3],
[6,3],
[6,6],
[3,6]]
/*-------------------------------------------------------------
Stampa dei risultati ottenuti dall'esecuzione delle due funzioni che ho scritto
-------------------------------------------------------------*/
function main(V,FV){
	console.log(vertici(V));
	console.log(facciate(FV));
}

/*-------------------------------------------------------------
Invocazione del metodo main
-------------------------------------------------------------*/
main(V,FV);