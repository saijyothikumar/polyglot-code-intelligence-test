// Intentional Java artifact inside experiments to test multi-language edges
public class LegacyJobRunner {
    public static void main(String[] args) {
        System.out.println("Running legacy job runner");
    }

    public String runJob(String name) {
        return "ran-" + name;
    }
}
