#include <stdio.h>
#include <stdlib.h>

#define MAX_CHAR 256

int main() {
    int val = 123456789;
    int count_1 = count_ones(val);
    int count_0 = count_zeros(val);
    char file_name = "ListaPalavrasEN.txt";
    char file_namePT = "ListaPalvrasPT.txt";
    char output_file_namePT = "Negative_WordListPT";
    char image = "..//lena.bmp";
    printf("val: %d\n", val);
    printf("count_ones result: %d\n", count_1);//should show count_ones result: 16
    printf("count_zeros result: %d\n", count_0);//should show count_zeros result: 11
    printf("print_bits result: ");
    print_bits(val);//should show print_bits result: 00000111010110111100110100010101
    //char most_frequent_1 = most_frequent_symbol(file_name);
    //printf("most frequent symbol: %d", most_frequent_1);
    negative_file(image,output_file_namePT);
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

// Função que retorna o simbolo mais frequente em um ficheiro representado por file_name
char most_frequent_symbol( char *file_name) {
    FILE *file_ptr;
    int freq[MAX_CHAR] = {0};
    char ch;
    int max_freq = 0;
    char most_freq_char;

    file_ptr = fopen(file_name, "r");
    if (file_ptr == NULL) {
        printf("Erro ao abrir arquivo.");
        exit(1);
    }

    // calcula a frequência de cada caractere no arquivo
    while ((ch = fgetc(file_ptr)) != EOF) {
        freq[ch]++;
    }

    // encontra o caractere mais frequente
    for (int i = 0; i < MAX_CHAR; i++) {
        if (freq[i] > max_freq) {
            max_freq = freq[i];
            most_freq_char = i;
        }
    }

    printf("O símbolo mais frequente no arquivo %s é '%c', ocorrendo %d vezes.\n", file_name, most_freq_char, max_freq);

    fclose(file_ptr);

    return most_freq_char;
}

//Função recebe um ficheiro de entrada input_file_name e abre no mode leitura binaria 
//e escreve cada bit negado no ficheiro output_file_name
void negative_file(char *input_file_name, char *output_file_name) {

    FILE *input_file = fopen(input_file_name, "rb");
    FILE *output_file = fopen(output_file_name, "wb");

    if (input_file == NULL) {
        printf("Erro ao abrir arquivo de entrada\n");
        return;
    }

    if (output_file == NULL) {
        printf("Erro ao criar arquivo de saída\n");
        return;
    }

    int c;
    while ((c = fgetc(input_file)) != EOF) {
        c = ~c; // negação de cada bit do caractere lido
        fputc(c, output_file);
    }

    fclose(input_file);
    fclose(output_file);
}