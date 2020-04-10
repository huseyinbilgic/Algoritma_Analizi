//Hüseyin Bilgiç 160401035

public class DynamicArray_myWork2 {
    int array[];
    int n;
    int kapasite;
    //constructor
    public DynamicArray_myWork2() {
        array = new int[2];// yeni 2 elemanlı boş bir array
        n = 0; // İçerisine eklenmiş olan eleman sayısı
        kapasite = 2;// Array' in kapasitesi
    }

    // Array' de sona eleman eklemek için

    //amortized cost
    //yeni eleman eklenmesi için n eleman yeni diziye kopyalanacaktır.
    //2n elemanı eklemek için n adet kopyalama gerekmektedir.
    //2n elemanın eklenmesi için 2n işlem + n adet kopyalama = 3n
    //O(3n/2n) = O(3/2) = O(1)
    public void append(int eleman) {
        // Kapasite yetersiz ise yeni array oluşturuldu.
        if (n == kapasite) {
            int yeni[] = new int[kapasite * 2];// Yeni eleman ekleneceğinden eski kapasitenin 2 katı kadarlık bir Array
                                               // oluşturuldu. ##complexity =>O(n)
            for (int i = 0; i < kapasite; i++) { // ##complexity =>O(n)
                yeni[i] = array[i];// array deki elemanları yedi diziye atıldı.
            }
            // kapasite ve yeni array atandı.
            array = yeni;
            kapasite = kapasite * 2;
        }
        // kapasite yeterliyse direk atama yapıldı.
        array[n] = eleman;
        n++;
    }

    // Array' den sondan eleman silmek için
    //amortized cost
    //O(1)
    public void remove() { 
        if (n > 0) {// Eğer array de eleman varsa sondan eleman silinmesi yapıldı. ##complexity=>O(5)~O(1)
            array[n - 1] = 0;
            n--;// Eleman silindiğinden eleman sayısı azaltıldı.
        }
    }

    // Array' e yeni kapasite vermek için
    //amortized cost
    //
    public void resize(int yeni_kapasite) {
        int temp[] = new int[yeni_kapasite];// yeni kapasite vermek için gönderilen parametre kadarlık Array
                                            // oluşturuldu.
        for (int i = 0; i < kapasite; i++) {
            temp[i] = array[i];// array deki elemanlar yeni Array' e atandı.
        }
        // Yeni kapasite ataması ve Array ataması yapıldı.
        array = temp;
        kapasite = yeni_kapasite;
    }

    public static void main(String args[]) {
        DynamicArray_myWork2 array = new DynamicArray_myWork2();

        System.out.println("Array elaman sayısı:" + array.n + ", Array kapasite: " + array.kapasite);
        //append için  örnek çağırımlar yapıldı.
        array.append(18);
        array.append(10);
        array.append(6);
        array.append(90);
        array.append(51);
        System.out.println("Array elaman sayısı:" + array.n + ", Array kapasite: " + array.kapasite);
        //remove için örnek çağırımlar yapıldı.
        array.remove();
        array.remove();
        array.remove();
        array.remove();
        array.remove();
        System.out.println("Array elaman sayısı:" + array.n + ", Array kapasite: " + array.kapasite);
        //resize için örnek çağırımlar yapıldı.
        array.resize(15);
        array.resize(20);
        array.resize(25);
        array.resize(30);
        array.resize(35);
        System.out.println("Array elaman sayısı:" + array.n + ", Array kapasite: " + array.kapasite);
    }
}
