import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertEquals;

/*
 * PLANO (Passo 1):
 * Problema: Calculadora de descontos para categorias de clientes (Comum, VIP e Premium).
 * Variações testadas:
 *   - Cliente COMUM (0% de desconto)
 *   - Cliente VIP (10% de desconto)
 *   - Cliente PREMIUM (20% de desconto)
 * Padrão escolhido: Strategy.
 */
public class CalculadoraDescontoTest {

    @Test
    void testDescontoClienteComum() {
        CalculadoraDesconto calc = new CalculadoraDesconto();
        assertEquals(100.0, calc.calcular("COMUM", 100.0));
    }

    @Test
    void testDescontoClienteVIP() {
        CalculadoraDesconto calc = new CalculadoraDesconto();
        assertEquals(90.0, calc.calcular("VIP", 100.0));
    }

    @Test
    void testDescontoClientePremium() {
        CalculadoraDesconto calc = new CalculadoraDesconto();
        assertEquals(80.0, calc.calcular("PREMIUM", 100.0));
    }
}