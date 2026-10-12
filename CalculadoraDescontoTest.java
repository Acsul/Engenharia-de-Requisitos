import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertEquals;

public class CalculadoraDescontoTest {
    @Test
    public void testCalcularDescontoComum() {
        CalculadoraDesconto calc = new CalculadoraDesconto();
        assertEquals(100.0, calc.calcular("Comum", 100.0));
    }

    @Test
    public void testCalcularDescontoVIP() {
        CalculadoraDesconto calc = new CalculadoraDesconto();
        assertEquals(90.0, calc.calcular("VIP", 100.0));
    }

    @Test
    public void testCalcularDescontoPremium() {
        CalculadoraDesconto calc = new CalculadoraDesconto();
        assertEquals(80.0, calc.calcular("Premium", 100.0));
    }
}

class CalculadoraDesconto {
    public double calcular(String cliente, double valor) {
        if (cliente.equals("Premium")){
            return valor*0.8;
        }else if (cliente.equals("VIP")){
            return valor*0.9;
        }else if (cliente.equals("Comum")){
            return valor*1;
        }else  {
            return valor;
        }
    }
}