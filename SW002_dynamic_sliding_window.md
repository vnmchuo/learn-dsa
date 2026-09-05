Pada **Dynamic (Variable-Size) Sliding Window**, ukuran jendela tidak lagi dipatok sebesar $k$. Jendela ini bergerak seperti seekor **ulat bulu (caterpillar)** atau akordeon:

1. **Kepala (`right`) melangkah maju:** Jendela melebar ke kanan untuk menelan elemen baru (*Expand*).
2. **Ekor (`left`) menyusul maju:** Jendela menciut dari kiri saat kondisi di dalam jendela melanggar aturan (*Shrink*).

```text
Kondisi Awal:             [ 2,  3,  1,  2,  4,  3 ]
                            ▲
                        left, right

Expand (right maju):      [ 2,  3,  1,  2,  4,  3 ]
                            ▲           ▲
                          left        right    -> Jendela melebar

Shrink (left menyusul):   [ 2,  3,  1,  2,  4,  3 ]
                                    ▲   ▲
                                  left right   -> Jendela menciut

```

---

### Dua Skenario Utama di Interview

Hampir semua soal tipe ini bermuara pada salah satu dari dua target berikut:

| Target Masalah | Logika Inti | Kapan Rekor Diperbarui? |
| --- | --- | --- |
| **Mencari Subarray Terpanjang** (Maksimum) | Perlebar jendela selama valid; ciutkan dari kiri jika melanggar batas. | **Di luar** loop `while` (saat jendela sudah valid). |
| **Mencari Subarray Terpendek** (Minimum) | Perlebar jendela sampai target tercapai; ciutkan dari kiri sebanyak mungkin untuk mencari ukuran terkecil. | **Di dalam** loop `while` (selama target masih terpenuhi). |

---

### Template Kerangka Berpikir (Mental Template)

Hampir 90% soal Dynamic Sliding Window dapat diselesaikan menggunakan pola kode standar ini:

```python
def dynamic_sliding_window(nums: list[int]) -> int:
    left = 0
    result = 0  # Atau float('inf') jika mencari nilai minimum
    window_state = 0  # Bisa berupa total sum, hash map / set frekuensi karakter, dll.

    # 1. EXPAND: right bergerak memperluas jendela
    for right in range(len(nums)):
        # Masukkan elemen baru nums[right] ke dalam jendela
        window_state += nums[right]

        # 2. SHRINK: ciutkan jendela dari kiri menggunakan while
        # Kondisi loop: selama jendela MELANGGAR aturan (atau SUDAH MEMENUHI target minimum)
        while window_state_melanggar_aturan:
            # Keluarkan nums[left] dari jendela
            window_state -= nums[left]
            # Majukan pointer kiri
            left += 1

        # 3. UPDATE RECORD: hitung panjang jendela saat ini: (right - left + 1)
        result = max(result, right - left + 1)

    return result

```

> **Catatan Rumus:** Panjang elemen sebuah jendela dari indeks `left` ke `right` selalu dihitung dengan:
> $$\text{Panjang Jendela} = \text{right} - \text{left} + 1$$
> 
> 

---

### Mengapa Tetap Bernilai $O(N)$?

Meskipun terlihat ada perulangan di dalam perulangan (`while` di dalam `for`), kompleksitas waktunya tetap **$O(N)$**.

Setiap elemen di dalam array maksimal hanya disentuh **2 kali**:

* 1 kali saat ditelan oleh pointer `right`.
* 1 kali saat dibuang oleh pointer `left`.

Karena pointer `left` hanya bergerak maju (tidak pernah mundur), total operasi pergeseran pointer dari awal hingga akhir maksimal hanya $2N$.