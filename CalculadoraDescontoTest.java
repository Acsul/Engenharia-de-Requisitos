import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertEquals;

public class CalculadoraDescontoTest {
    @Test
    public void testCalcularDescontoComum() {
        CalculadoraDesconto calc = new CalculadoraDesconto();
        assertEquals(100.0, calc.calcular("comum", 100.0));
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
