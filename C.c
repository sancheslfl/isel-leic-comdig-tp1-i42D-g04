//Função que retorna o numero de bits a 1 no valor inteiro val
int count_ones(int val) {
    int count = 0;
    while (val != 0) {
        if (val & 1) {
            count++;
        }
        val >>= 1;
    }
    return count;
}

//Função que retorna o numero de bits a 0 no valor inteiro val
int count_zeros(int val) {
    int count = 0;
    while (val != 0) {
        if ((val & 1) == 0) {
            count++;
        }
        val >>= 1;
    }
    return count;
}
void print_bits( int val ){//a qual imprime como caracteres os valores dos bits de todos os elementos fo valor inteiro val, passado como parâmetro.

}
char most_frequent_symbol( char *file_name ){// a qual retorna o símbolo mais frequente do ficheiro
//de texto file_name. A função imprime na consola o número de vezes que esse símbolo ocorre no ficheiro.

}
void negative_file( char *input_file_name, char *output_file_name){//a qual transforma o ficheiro
//de entrada input_file_name no ficheiro de saída output_file_name. O ficheiro de saída é produzido a partir do
//ficheiro de entrada através na negação de cada bit do mesmo.


}