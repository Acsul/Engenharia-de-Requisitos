import java.util.Map;
import java.util.HashMap;

// Padrão de Projeto Aplicado: STRATEGY
interface EstrategiaDesconto {
    double calcularDesconto(double valor);
}

class DescontoComum implements EstrategiaDesconto {
    public double calcularDesconto(double valor) { return valor; }
}

class DescontoVIP implements EstrategiaDesconto {
    public double calcularDesconto(double valor) { return valor * 0.9; }
}

class DescontoPremium implements EstrategiaDesconto {
    public double calcularDesconto(double valor) { return valor * 0.8; }
}

public class CalculadoraDesconto {
    private final Map<String, EstrategiaDesconto> estrategias;

    public CalculadoraDesconto() {
        estrategias = new HashMap<>();
        estrategias.put("COMUM", new DescontoComum());
        estrategias.put("VIP", new DescontoVIP());
        estrategias.put("PREMIUM", new DescontoPremium());
    }

    public double calcular(String tipoCliente, double valor) {
        EstrategiaDesconto estrategia = estrategias.getOrDefault(tipoCliente, new DescontoComum());
        return estrategia.calcularDesconto(valor);
    }
}

/*
* AUTOAVALIAÇÃO:
*
* Eu fiz um projeto simples quera somente atribuir descontos a produtos a minha maior dificuldade foi de refatorar o projeto pois tinha que aplicar
* um padrão de projeto que dá mais trabalho.
* */