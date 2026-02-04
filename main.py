import os

# Fungsi untuk membersihkan layar
def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

# Daftar tugas: list of dicts dengan 'task' dan 'done'
tasks = []

def show_menu():
    print("\n" + "="*40)
    print("     Aplikasi To-Do List untuk Anak Sekolah")
    print("="*40)
    print("1. Tambah Tugas")
    print("2. Lihat Semua Tugas")
    print("3. Tandai Tugas Selesai")
    print("4. Hapus Tugas")
    print("5. Keluar")
    print("="*40)

def add_task():
    task = input("Masukkan tugas baru: ")
    tasks.append({"task": task, "done": False})
    print(f"Tugas '{task}' telah ditambahkan! Semangat ya!")

def view_tasks():
    if not tasks:
        print("Belum ada tugas. Tambahkan tugas dulu!")
        return
    print("\nDaftar Tugas:")
    for i, task in enumerate(tasks, 1):
        status = "✅" if task["done"] else "☐"
        print(f"{i}. {status} {task['task']}")

def mark_done():
    view_tasks()
    if not tasks:
        return
    try:
        num = int(input("Masukkan nomor tugas yang sudah selesai: ")) - 1
        if 0 <= num < len(tasks):
            tasks[num]["done"] = True
            print(f"Tugas '{tasks[num]['task']}' ditandai selesai! Bagus!")
        else:
            print("Nomor tugas tidak valid.")
    except ValueError:
        print("Masukkan nomor yang benar.")

def delete_task():
    view_tasks()
    if not tasks:
        return
    try:
        num = int(input("Masukkan nomor tugas yang ingin dihapus: ")) - 1
        if 0 <= num < len(tasks):
            removed = tasks.pop(num)
            print(f"Tugas '{removed['task']}' telah dihapus.")
        else:
            print("Nomor tugas tidak valid.")
    except ValueError:
        print("Masukkan nomor yang benar.")

def main():
    clear_screen()
    print("Selamat datang di To-Do List Sekolah!")
    print("Mari kita atur tugas-tugasmu agar lebih tertib.")

    while True:
        show_menu()
        choice = input("Pilih menu (1-5): ")
        clear_screen()

        if choice == '1':
            add_task()
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            mark_done()
        elif choice == '4':
            delete_task()
        elif choice == '5':
            print("Terima kasih telah menggunakan To-Do List! Sampai jumpa!")
            break
        else:
            print("Pilihan tidak valid. Coba lagi.")

        input("\nTekan Enter untuk melanjutkan...")

if __name__ == "__main__":
    main()
