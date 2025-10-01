# Styra ett relä med BeagleBone

Detta exempel visar hur du kan styra ett relä via en GPIO‑pinne på BeagleBone Black.

---

## 🛠️ Hårdvara
- **BeagleBone Black**
- **Relämodul** (3.3 V logiknivå)
- **Koppling:**
  - Pin 1 → GND
  - Pin 2 → 3.3 V (VCC)
  - Pin 12 → GPIO (styrsignal)

> Obs: Se till att relämodulen är avsedd för 3.3 V logik.  
> Om du använder ett “naket” relä behöver du en transistor + diod för att skydda BeagleBone.

---

# 📦 Installation
#Installera I2C‑verktyg och Python‑bibliotek (för andra projekt, inte nödvändigt för just relästyrning men bra att ha):

```bash
sudo apt-get update
sudo apt-get install -y python3-smbus i2c-tools

när du kopplad sensorn ti beagle boarden så använd i2cdetect -y 2 eller i2cdetect -y 1. Siffran efter -y är i2c bussen
 
 

