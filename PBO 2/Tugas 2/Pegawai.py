import tkinter as tk
from tkinter import ttk

class Pegawai:
    def __init__(self, nama, nip):
        self.nama = nama
        self.nip = nip

    def get_nama(self):
        return self.nama

    def get_nip(self):
        return self.nip

class PegawaiTetap(Pegawai):
    def __init__(self, nama, nip, gaji_pokok):
        super().__init__(nama, nip)
        self.gaji_pokok = gaji_pokok

    def get_gaji_pokok(self):
        return self.gaji_pokok

class PegawaiHarian(Pegawai):
    def __init__(self, nama, nip, upah_per_hari):
        super().__init__(nama, nip)
        self.upah_per_hari = upah_per_hari

    def get_upah_per_hari(self):
        return self.upah_per_hari

class PegawaiKontrak(Pegawai):
    def __init__(self, nama, nip, upah_per_bulan):
        super().__init__(nama, nip)
        self.upah_per_bulan = upah_per_bulan

    def get_upah_per_bulan(self):
        return self.upah_per_bulan

# Tampilan interaktif
def main():
    root = tk.Tk()
    root.title("Data Pegawai")

    def tambah_pegawai():
        nama = entry_nama.get()
        nip = entry_nip.get()
        jenis = jenis_var.get()

        if jenis == "Pegawai Tetap":
            gaji_pokok = entry_gaji_pokok.get()
            pegawai = PegawaiTetap(nama, nip, gaji_pokok)
        elif jenis == "Pegawai Harian":
            upah_per_hari = entry_upah_per_hari.get()
            pegawai = PegawaiHarian(nama, nip, upah_per_hari)
        elif jenis == "Pegawai Kontrak":
            upah_per_bulan = entry_upah_per_bulan.get()
            pegawai = PegawaiKontrak(nama, nip, upah_per_bulan)
        else:
            pegawai = Pegawai(nama, nip)

        daftar_pegawai.append(pegawai)
        clear_entries()
        result_label.config(text=f"{jenis} berhasil ditambahkan.")

    def clear_entries():
        entry_nama.delete(0, "end")
        entry_nip.delete(0, "end")
        entry_gaji_pokok.delete(0, "end")
        entry_upah_per_hari.delete(0, "end")
        entry_upah_per_bulan.delete(0, "end")

    def lihat_daftar():
        daftar_label.config(text="Daftar Pegawai:")
        daftar_text.config(state="normal")
        daftar_text.delete(1.0, "end")

        for pegawai in daftar_pegawai:
            daftar_text.insert("end", f"Nama: {pegawai.get_nama()}, NIP: {pegawai.get_nip()}\n")

            if isinstance(pegawai, PegawaiTetap):
                daftar_text.insert("end", f"Gaji Pokok: {pegawai.get_gaji_pokok()}\n")
            elif isinstance(pegawai, PegawaiHarian):
                daftar_text.insert("end", f"Upah per Hari: {pegawai.get_upah_per_hari()}\n")
            elif isinstance(pegawai, PegawaiKontrak):
                daftar_text.insert("end", f"upah per Bulan: {pegawai.get_upah_per_bulan()}\n")

            daftar_text.insert("end", "\n")

        daftar_text.config(state="disabled")


    def update_entry_fields():
        jenis = jenis_var.get()
        if jenis == "Pegawai Tetap":
            label_gaji_pokok.grid(row=2, column=0, sticky="W")
            entry_gaji_pokok.grid(row=2, column=1, sticky="EW")
            label_upah_per_hari.grid_remove()
            entry_upah_per_hari.grid_remove()
            label_upah_per_bulan.grid_remove()
            entry_upah_per_bulan.grid_remove()
        elif jenis == "Pegawai Harian":
            label_gaji_pokok.grid_remove()
            entry_gaji_pokok.grid_remove()
            label_upah_per_hari.grid(row=2, column=0, sticky="W")
            entry_upah_per_hari.grid(row=2, column=1, sticky="EW")
            label_upah_per_bulan.grid_remove()
            entry_upah_per_bulan.grid_remove()
        elif jenis == "Pegawai Kontrak":
            label_gaji_pokok.grid_remove()
            entry_gaji_pokok.grid_remove()
            label_upah_per_hari.grid_remove()
            entry_upah_per_hari.grid_remove()
            label_upah_per_bulan.grid(row=2, column=0, sticky="W")
            entry_upah_per_bulan.grid(row=2, column=1, sticky="EW")
        else:
            label_gaji_pokok.grid_remove()
            entry_gaji_pokok.grid_remove()
            label_upah_per_hari.grid_remove()
            entry_upah_per_hari.grid_remove()
            label_upah_per_bulan.grid_remove()
            entry_upah_per_bulan.grid_remove()

    frame_input = ttk.Frame(root)
    frame_input.pack(padx=10, pady=10)

    label_nama = ttk.Label(frame_input, text="Nama:")
    label_nama.grid(row=0, column=0, sticky="W")
    entry_nama = ttk.Entry(frame_input)
    entry_nama.grid(row=0, column=1, sticky="EW")

    label_nip = ttk.Label(frame_input, text="NIP:")
    label_nip.grid(row=1, column=0, sticky="W")
    entry_nip = ttk.Entry(frame_input)
    entry_nip.grid(row=1, column=1, sticky="EW")

    label_gaji_pokok = ttk.Label(frame_input, text="Gaji Pokok:")
    label_gaji_pokok.grid(row=2, column=0, sticky="W")
    entry_gaji_pokok = ttk.Entry(frame_input)
    entry_gaji_pokok.grid(row=2, column=1, sticky="EW")

    label_upah_per_hari = ttk.Label(frame_input, text="Upah per Hari:")
    label_upah_per_hari.grid(row=2, column=0, sticky="W")
    entry_upah_per_hari = ttk.Entry(frame_input)
    entry_upah_per_hari.grid(row=2, column=1, sticky="EW")

    label_upah_per_bulan = ttk.Label(frame_input, text="Upah per Bulan:")
    label_upah_per_bulan.grid(row=2, column=0, sticky="W")
    entry_upah_per_bulan = ttk.Entry(frame_input)
    entry_upah_per_bulan.grid(row=2, column=1, sticky="EW")

    label_jenis = ttk.Label(frame_input, text="Jenis Pegawai:")
    label_jenis.grid(row=3, column=0, sticky="W")
    jenis_var = tk.StringVar()
    jenis_combo = ttk.Combobox(frame_input, textvariable=jenis_var, values=["Pegawai Tetap", "Pegawai Harian", "Pegawai Kontrak"])
    jenis_combo.grid(row=3, column=1, sticky="EW")

    result_label = ttk.Label(frame_input, text="")
    result_label.grid(row=5, column=0, columnspan=2)

    tambah_button = ttk.Button(frame_input, text="Tambah Pegawai", command=tambah_pegawai)
    tambah_button.grid(row=4, column=0, columnspan=2)

    # Update fields based on jenis selection
    jenis_combo.bind("<<ComboboxSelected>>", lambda event: update_entry_fields())

    def lihat_daftar():
        daftar_label.config(text="Daftar Pegawai:")
        daftar_text.config(state="normal")
        daftar_text.delete(1.0, "end")

        for pegawai in daftar_pegawai:
            daftar_text.insert("end", f"Nama: {pegawai.get_nama()}, NIP: {pegawai.get_nip()}\n")

            if isinstance(pegawai, PegawaiTetap):
                daftar_text.insert("end", f"Gaji Pokok: {pegawai.get_gaji_pokok()}\n")
            elif isinstance(pegawai, PegawaiHarian):
                daftar_text.insert("end", f"Upah per Hari: {pegawai.get_upah_per_hari()}\n")
            elif isinstance(pegawai, PegawaiKontrak):
                daftar_text.insert("end", f"Upah per Bulan: {pegawai.get_upah_per_bulan()}\n")

            daftar_text.insert("end", "\n")

        daftar_text.config(state="disabled")

    frame_daftar = ttk.Frame(root)
    frame_daftar.pack(padx=10, pady=10)

    daftar_pegawai = []

    daftar_label = ttk.Label(frame_daftar, text="")
    daftar_label.grid(row=0, column=0, sticky="W")

    daftar_button = ttk.Button(frame_daftar, text="Lihat Daftar Pegawai", command=lihat_daftar)
    daftar_button.grid(row=0, column=1)

    daftar_text = tk.Text(frame_daftar, state="disabled", wrap="none", height=10, width=50)
    daftar_text.grid(row=1, column=0, columnspan=2)

    root.mainloop()

if __name__ == "__main__":
    main()
