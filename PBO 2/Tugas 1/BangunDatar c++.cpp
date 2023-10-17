#include <iostream>
#include <cmath>

class BangunDatar {
public:
    virtual double hitungLuas() = 0;
    virtual double hitungKeliling() = 0;
};

class Persegi : public BangunDatar {
private:
    double sisi;

public:
    Persegi(double sisi) : sisi(sisi) {}

    double hitungLuas() override {
        return sisi * sisi;
    }

    double hitungKeliling() override {
        return 4 * sisi;
    }
};

class PersegiPanjang : public BangunDatar {
private:
    double panjang;
    double lebar;

public:
    PersegiPanjang(double panjang, double lebar) : panjang(panjang), lebar(lebar) {}

    double hitungLuas() override {
        return panjang * lebar;
    }

    double hitungKeliling() override {
        return 2 * (panjang + lebar);
    }
};

class Segitiga : public BangunDatar {
private:
    double alas;
    double tinggi;
    double sisi2;
    double sisi3;

public:
    Segitiga(double alas, double tinggi, double sisi2, double sisi3) : alas(alas), tinggi(tinggi), sisi2(sisi2), sisi3(sisi3) {}

    double hitungLuas() override {
        return 0.5 * alas * tinggi;
    }

    double hitungKeliling() override {
        return alas + sisi2 + sisi3;
    }
};

class Lingkaran : public BangunDatar {
private:
    double jariJari;

public:
    Lingkaran(double jariJari) : jariJari(jariJari) {}

    double hitungLuas() override {
        return 3.14159265 * jariJari * jariJari;
    }

    double hitungKeliling() override {
        return 2 * 3.14159265 * jariJari;
    }
};

int main() {
    Persegi persegi(5);
    PersegiPanjang persegiPanjang(4, 6);
    Segitiga segitiga(6, 8, 5, 5);
    Lingkaran lingkaran(3);

    std::cout << "Luas dan Keliling Persegi:" << std::endl;
    std::cout << "Luas: " << persegi.hitungLuas() << std::endl;
    std::cout << "Keliling: " << persegi.hitungKeliling() << std::endl;

    std::cout << "\nLuas dan Keliling Persegi Panjang:" << std::endl;
    std::cout << "Luas: " << persegiPanjang.hitungLuas() << std::endl;
    std::cout << "Keliling: " << persegiPanjang.hitungKeliling() << std::endl;

    std::cout << "\nLuas dan Keliling Segitiga:" << std::endl;
    std::cout << "Luas: " << segitiga.hitungLuas() << std::endl;
    std::cout << "Keliling: " << segitiga.hitungKeliling() << std::endl;

    std::cout << "\nLuas dan Keliling Lingkaran:" << std::endl;
    std::cout << "Luas: " << lingkaran.hitungLuas() << std::endl;
    std::cout << "Keliling: " << lingkaran.hitungKeliling() << std::endl;

    return 0;
}

