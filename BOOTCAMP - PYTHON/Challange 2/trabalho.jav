import java.util.ArrayList;
import java.util.Scanner;

// Classe abstrata que representa uma moeda genérica
abstract class Moeda {
    protected double valor; // Valor da moeda em sua própria moeda (Real, Dólar, Euro, etc.)

    public Moeda(double valor) {
        this.valor = valor;
    }

    public double getValor() {
        return valor;
    }

    // Método abstrato para obter o valor da moeda convertido para Real
    public abstract double getValorEmReal();
}

// Classe que representa uma moeda específica (Real)
class Real extends Moeda {
    public Real(double valor) {
        super(valor);
    }

    @Override
    public double getValorEmReal() {
        return valor; // Como é Real, não é necessário fazer conversão
    }
}

// Classe que representa uma moeda específica (Dólar)
class Dolar extends Moeda {
    public Dolar(double valor) {
        super(valor);
    }

    @Override
    public double getValorEmReal() {
        // Aqui você colocaria a lógica de conversão de Dólar para Real
        // Para simplificar, vamos assumir que 1 Dólar equivale a 5 Reais
        return valor * 5;
    }
}

// Classe que representa uma moeda específica (Euro)
class Euro extends Moeda {
    public Euro(double valor) {
        super(valor);
    }

    @Override
    public double getValorEmReal() {
        // Aqui você colocaria a lógica de conversão de Euro para Real
        // Para simplificar, vamos assumir que 1 Euro equivale a 6 Reais
        return valor * 6;
    }
}

// Classe que representa o cofrinho que armazena as moedas
class Cofrinho {
    private ArrayList<Moeda> moedas; // Lista de moedas no cofrinho

    public Cofrinho() {
        moedas = new ArrayList<>();
    }

    // Método para adicionar uma moeda ao cofrinho
    public void adicionarMoeda(Moeda moeda) {
        moedas.add(moeda);
    }

    // Método para remover uma moeda específica do cofrinho
    public void removerMoeda(Moeda moeda) {
        moedas.remove(moeda);
    }

    // Método para listar todas as moedas no cofrinho
    public void listarMoedas() {
        System.out.println("Moedas no cofrinho:");
        for (Moeda moeda : moedas) {
            System.out.println("- " + moeda.getClass().getSimpleName() + ": " + moeda.getValor());
        }
    }

    // Método para calcular o valor total do cofrinho em Reais
    public double calcularValorTotalEmReal() {
        double total = 0;
        for (Moeda moeda : moedas) {
            total += moeda.getValorEmReal();
        }
        return total;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Cofrinho cofrinho = new Cofrinho();

        while (true) {
            // Menu de opções
            System.out.println("\nMenu:");
            System.out.println("1. Adicionar moeda");
            System.out.println("2. Remover moeda");
            System.out.println("3. Listar moedas");
            System.out.println("4. Calcular valor total em Real");
            System.out.println("5. Sair");
            System.out.print("Escolha uma opção: ");
            int opcao = scanner.nextInt();

            switch (opcao) {
                case 1:
                    System.out.println("\nEscolha o tipo de moeda:");
                    System.out.println("1. Real");
                    System.out.println("2. Dólar");
                    System.out.println("3. Euro");
                    System.out.print("Opção: ");
                    int tipoMoeda = scanner.nextInt();
                    System.out.print("Valor da moeda: ");
                    double valorMoeda = scanner.nextDouble();

                    // Adiciona a moeda ao cofrinho de acordo com a escolha do usuário
                    switch (tipoMoeda) {
                        case 1:
                            cofrinho.adicionarMoeda(new Real(valorMoeda));
                            break;
                        case 2:
                            cofrinho.adicionarMoeda(new Dolar(valorMoeda));
                            break;
                        case 3:
                            cofrinho.adicionarMoeda(new Euro(valorMoeda));
                            break;
                        default:
                            System.out.println("Opção inválida.");
                    }
                    break;
                case 2:
                    // Remover moeda
                    // (Implementação deixada como exercício)
                    break;
                case 3:
                    // Listar moedas
                    cofrinho.listarMoedas();
                    break;
                case 4:
                    // Calcular valor total em Real
                    double valorTotalEmReal = cofrinho.calcularValorTotalEmReal();
                    System.out.println("Valor total em Real: R$ " + valorTotalEmReal);
                    break;
                case 5:
                    // Sair do programa
                    System.out.println("Saindo...");
                    return;
                default:
                    System.out.println("Opção inválida.");
            }
        }
    }
}
