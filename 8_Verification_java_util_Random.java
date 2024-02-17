/**
 * Proof of Concept permettant de vérifier que la fonction java.util.Random n'est pas sécurisée à cause de son manque d'entropie.
 * Deux instances ayant la même seed et créées au même moment donneront les mêmes resultats.
 * Il faut utiliser la fonction java.security.SecureRandom à la place
 */

import java.util.Random;

public class Example {
    public static void main(String[] args) {
        Random r1 = new Random(42);
        Random r2 = new Random(42);
        int x, y;

        for (int i = 0; i < 10; i++) {
            x = r1.nextInt();
            y = r2.nextInt();
            
            if (x == y) {
                System.out.println("They match! " + x);
            }
        }
    }
}
