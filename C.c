#include <stdio.h>

int main() {
    int val = 123456789;
    int count_1 = count_ones(val);
    printf("result: %d\n", count_1);
    printf("result: %d", count_zeros(val));
}


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

//Função que escreve o valor em binario introduzido em val
void print_bits(int val) {
    int i;
    for (i = sizeof(int) * 8 - 1; i >= 0; i--) {
        if (val & (1 << i)) {
            printf("1");
        } else {
            printf("0");
        }
    }
    printf("\n");
}
char most_frequent_symbol( char *file_name ){// a qual retorna o símbolo mais frequente do ficheiro
//de texto file_name. A função imprime na consola o número de vezes que esse símbolo ocorre no ficheiro.

}
void negative_file( char *input_file_name, char *output_file_name){//a qual transforma o ficheiro
//de entrada input_file_name no ficheiro de saída output_file_name. O ficheiro de saída é produzido a partir do
//ficheiro de entrada através na negação de cada bit do mesmo.


}