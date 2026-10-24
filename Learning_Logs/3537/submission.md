# บันทึกการแก้โจทย์

ไฟล์นี้ต้องเขียนโดยนักศึกษาด้วยคำพูดของตนเอง

ใช้ template นี้เฉพาะกับโจทย์ OJ ที่ถูกระบุว่าต้องส่ง learning log เท่านั้น

ห้ามให้ AI เขียนไฟล์นี้แทนคุณ AI อาจช่วยตรวจ grammar, formatting หรือความชัดเจนได้ หลังจากที่คุณเขียนเนื้อหาของตนเองแล้ว

ถ้าใช้ AI กับโจทย์ learning-log-required นี้ ต้องทำไฟล์ `ai_reflection.md` ด้วย

---

## 1. ข้อมูล OJ

หมายเลข/ชื่อโจทย์ OJ:

```text
OJ3537 - [LEARNING LOGS] Impostor
```

OJ submission ID ถ้ามีการส่งแล้ว:

```text
696296
```

สถานะ OJ:

```text
Pass
```

เวลาที่ใช้คิดและทำโจทย์ด้วยตนเอง:

```text
1-3 hours
```

เลือกหนึ่งข้อ:

```text
0-15 minutes
15-30 minutes
30-60 minutes
1-3 hours
3-6 hours
6-24 hours
1-3 days
4-7 days
1-4 weeks
More than 4 weeks
```

วิธีนับเวลา:

- นับเฉพาะเวลาที่ตั้งใจทำโจทย์นี้ด้วยตนเองจริง ๆ
- เริ่มนับตั้งแต่ตอนที่อ่านโจทย์ครั้งแรก
- ไม่นับเวลาพัก กินข้าว เรียน นอน เวลาที่ทำโจทย์อื่น หรือเวลาที่ไม่ได้ทำโจทย์นี้
- ถ้าใช้ AI ให้นับเฉพาะเวลาที่ทำด้วยตนเองก่อน prompt แรกที่ถาม AI
- ถ้าถามเพื่อน TA หรือผู้สอน ให้นับเฉพาะเวลาที่ทำด้วยตนเองก่อนขอความช่วยเหลือครั้งแรก
- ถ้าใช้ทั้ง AI และความช่วยเหลือจากคน ให้นับเฉพาะเวลาที่ทำด้วยตนเองก่อนขอความช่วยเหลือจากภายนอกครั้งแรก ไม่ว่าจะเป็น AI หรือคน
- ถ้าไม่ได้ใช้ AI และไม่ได้ขอความช่วยเหลือจากคน ให้นับเวลาถึงก่อนเขียน `submission.md`
- ประมาณเวลาได้ แต่ต้องซื่อสัตย์

---

## 2. ความเข้าใจโจทย์ของฉัน

เขียนโจทย์ด้วยคำพูดของตนเอง

ให้อธิบาย input, output และ constraints สำคัญด้วย

ถ้ายังไม่เข้าใจโจทย์ทั้งหมด ให้เขียนสิ่งที่เข้าใจในตอนนี้ ความเข้าใจอาจยังไม่ครบหรืออาจผิดได้ แต่ต้องพยายามอธิบายอย่างจริงใจ

```text
โจทย์นี้ให้รับข้อมูลผู้เล่นในยานอวกาศ แต่ละบรรทัดเป็น dict เช่น {"Green" : "Crewmate"} บอกชื่อกับบทบาท (Crewmate หรือ Impostor) รับไปเรื่อยๆ จนเจอคำว่า Start จากนั้นรับชื่อคนที่ถูกโหวตไล่ออกจนเจอคำว่า End แล้วพิมพ์จำนวน Impostor ที่ยังเหลืออยู่ ตามด้วยรายชื่อคนที่ยังอยู่ (Alive) และคนที่ถูกไล่ออก (Dead) เรียงตามตัวอักษร เช่น ตัวอย่างในโจทย์ Green, Cyan, White ถูกไล่ออก เหลือ Impostor 2 คน (Blue กับ Lime) ได้ 2 Impostor Remains

ส่วน input ช่วงแรกคือ dict ทีละบรรทัดจนถึง Start ช่วงที่สองคือชื่อทีละบรรทัดจนถึง End ส่วน output บรรทัดแรกคือ <จำนวน> Impostor Remains ตามด้วย ***Alive*** แล้วตามด้วยรายชื่อคนที่ยังอยู่ในรูป ชื่อ : บทบาท จากนั้น ***Dead*** แล้วตามด้วยรายชื่อคนที่ถูกไล่ออกในรูปเดียวกัน โดยเรียงตามชื่อทั้งสองกลุ่ม โจทย์ยังแนะนำให้ใช้ dict กับ method ของ dict ด้วย

สิ่งที่ผมต้องระวังคือรูปแบบ output ต้องเป็น ชื่อ : บทบาท มีเว้นวรรคหน้าหลังเครื่องหมาย : และต้องเรียงตามตัวอักษรทั้งกลุ่ม Alive และ Dead รวมถึงต้องนับ Impostor เฉพาะคนที่ยังเหลืออยู่ ไม่นับคนที่ถูกไล่ออกไปแล้ว
```

---

## 3. แผนแรกของฉัน

เขียนแผนแรกก่อนรับความช่วยเหลือจาก AI เพื่อน TA ผู้สอน หรือก่อนสรุป code สุดท้าย

ถ้าใช้ AI ให้เขียนแผนที่มีอยู่ก่อน prompt แรกที่ถาม AI

ถ้าถามเพื่อน TA หรือผู้สอน ให้เขียนแผนที่มีอยู่ก่อนถาม

ถ้าไม่ได้ใช้ AI และไม่ได้ขอความช่วยเหลือจากคน ให้เขียนแผนที่มีอยู่ก่อนหรือระหว่างเริ่มเขียน code

แผนนี้เขียนแบบคร่าว ๆ ได้ อาจยังไม่สมบูรณ์หรืออาจต่างจากวิธีสุดท้าย

สามารถเขียนเป็น pseudocode, flowchart idea หรือขั้นตอนความคิดได้

```text
Step 1: สร้าง dict alive ว่างไว้ แล้ววนรับข้อมูลทีละบรรทัดจนเจอ Start แต่ละบรรทัดแปลงเป็น dict ด้วย ast.literal_eval แล้วรวมเข้า alive ด้วย update
Step 2: สร้าง dict dead ว่างไว้ แล้ววนรับชื่อทีละบรรทัดจนเจอ End ถ้าชื่อนั้นอยู่ใน alive ให้เอาออกจาก alive ด้วย pop แล้วเก็บลง dead พร้อมบทบาท
Step 3: นับ Impostor ที่เหลือจากค่าใน alive ด้วย count("Impostor")
Step 4: พิมพ์จำนวน Impostor ตามด้วย ***Alive*** แล้ววนพิมพ์ alive ที่เรียงตามชื่อด้วย sorted(alive.items())
Step 5: พิมพ์ ***Dead*** แล้ววนพิมพ์ dead ที่เรียงตามชื่อแบบเดียวกัน
ส่วนที่ผมยังไม่แน่ใจคือจะแปลงข้อความหน้าตาเป็น dict ในแต่ละบรรทัดให้เป็น dict จริงๆ ได้ยังไง และกรณีที่ไม่มีใครถูกไล่ออกเลย (Dead จะว่าง) ผมเลยวางแผนว่าจะลองเทสต์กรณีนี้ด้วย
```

---

## 4. วิธีสุดท้ายที่ใช้จริง

อธิบายสั้น ๆ ว่า algorithm หรือวิธีสุดท้ายที่ใช้จริงใน code ที่ส่งคืออะไร

หัวข้อนี้ต่างจาก Section 3:

- Section 3 คือแผนแรกก่อนใช้ AI ก่อนรับความช่วยเหลือจากคน หรือก่อนเขียน code สุดท้าย
- Section 4 คือวิธีสุดท้ายที่ใช้ใน solution จริง
- ถ้าวิธีสุดท้ายเหมือนกับแผนแรก ให้เขียนว่าเหมือนกัน และอธิบายสั้น ๆ ว่าทำไม

ห้ามคัดลอกคำอธิบายจาก AI

ห้ามคัดลอกคำอธิบายจากคนอื่น

```text
วิธีสุดท้ายที่ใช้จริง เหมือนแผนแรก ผมแปลงแต่ละบรรทัดเป็น dict ด้วย ast.literal_eval แล้ว update เข้า alive จากนั้นเอาคนที่ถูกโหวตออกด้วย pop ไปเก็บใน dead แล้วใช้ sorted(...items()) เรียงตามชื่อตอนพิมพ์ ที่ใช้วิธีนี้เพราะโจทย์แนะนำให้ใช้ dict และ method ของมัน ซึ่งทำให้ย้ายคนจากกลุ่มที่ยังอยู่ไปกลุ่มที่ถูกไล่ออกได้ง่าย โดยไม่ต้องเก็บบทบาทแยกอีกลิสต์ และไม่ต้องเขียนลูปค้นหาเอง
```

---

## 5. การทดสอบของฉัน

เขียน test cases อย่างน้อย 3 กรณีที่ลองเองหรือออกแบบเอง

พยายามเลือก test cases ที่แตกต่างกัน

แต่ละ test case ให้อธิบายว่าทำไมเลือกกรณีนั้น

ถ้า input หรือ output มีหลายบรรทัด ให้เขียนไว้ใน text blocks

### Test Case 1

ทำไมเลือก case นี้:

```text
เป็น case ปกติจากตัวอย่างในโจทย์ มีทั้ง Crewmate และ Impostor และมีคนถูกไล่ออกหลายคน ใช้เช็กรูปแบบ output ทั้งหมดและการเรียงตามชื่อ
```

Input:

```text
{"Green" : "Crewmate"} / {"Cyan" : "Crewmate"} / {"Red" : "Crewmate"} / {"Pink" : "Crewmate"} / {"Lime" : "Impostor"} / {"Blue" : "Impostor"} / {"White" : "Crewmate"} / {"Orange" : "Crewmate"} / Start / Green / Cyan / White / End
```

Expected output:

```text
2 Impostor Remains / ***Alive*** / Blue : Impostor / Lime : Impostor / Orange : Crewmate / Pink : Crewmate / Red : Crewmate / ***Dead*** / Cyan : Crewmate / Green : Crewmate / White : Crewmate
```

Actual output:

```text
2 Impostor Remains / ***Alive*** / Blue : Impostor / Lime : Impostor / Orange : Crewmate / Pink : Crewmate / Red : Crewmate / ***Dead*** / Cyan : Crewmate / Green : Crewmate / White : Crewmate
```

Result:

```text
Pass
```

### Test Case 2

ทำไมเลือก case นี้:

```text
เป็น case เล็กสุด คือมีผู้เล่นคนเดียวและไม่มีใครถูกไล่ออกเลย ใช้เช็กว่าโปรแกรมไม่ error เมื่อ Dead ว่าง และยังพิมพ์หัวข้อ ***Dead*** ออกมา
```

Input:

```text
{"Red" : "Impostor"} / Start / End
```

Expected output:

```text
1 Impostor Remains / ***Alive*** / Red : Impostor / ***Dead***
```

Actual output:

```text
1 Impostor Remains / ***Alive*** / Red : Impostor / ***Dead***
```

Result:

```text
Pass
```

### Test Case 3

ทำไมเลือก case นี้:

```text
เป็น case ที่ Impostor ถูกไล่ออกหมดทุกคน ใช้เช็กว่านับ Impostor ที่เหลือได้เป็น 0 และ Alive มีแต่ Crewmate
```

Input:

```text
{"Blue" : "Crewmate"} / {"Red" : "Impostor"} / Start / Red / End
```

Expected output:

```text
0 Impostor Remains / ***Alive*** / Blue : Crewmate / ***Dead*** / Red : Impostor
```

Actual output:

```text
0 Impostor Remains / ***Alive*** / Blue : Crewmate / ***Dead*** / Red : Impostor
```

Result:

```text
Pass
```

---

## 6. การใช้ AI

ใช้ AI กับโจทย์นี้หรือไม่

```text
No
```

ถ้าใช้ AI ต้องทำไฟล์นี้ด้วย:

```text
ai_reflection.md
```

ถ้าถามเฉพาะเพื่อน TA หรือผู้สอน และไม่ได้ใช้ AI ไม่ต้องทำ `ai_reflection.md`

---

## 7. ความช่วยเหลือจากคน / การร่วมมือ

ได้ถามเพื่อน TA ผู้สอน หรือบุคคลอื่นเพื่อขอความช่วยเหลือในโจทย์นี้หรือไม่

```text
No
```

ถ้าใช่ ให้อธิบายสั้น ๆ ว่าได้รับความช่วยเหลือแบบใด

ตัวอย่างที่อนุญาต:

- อธิบายความหมายของโจทย์
- อธิบาย concept การเขียนโปรแกรม
- ให้ hint เกี่ยวกับแนวทาง
- คุยเรื่อง debugging
- คุยเรื่อง test cases
- ช่วยอธิบาย error message

สิ่งที่ไม่อนุญาต:

- คัดลอก code ของผู้อื่น
- ส่ง solution ของผู้อื่น
- ขอให้ผู้อื่นเขียน solution ให้
- ใช้ OJ submission ของผู้อื่น
- ขอให้ผู้อื่นส่ง OJ แทน

ใครช่วยคุณ

```text

```

เขาช่วยอะไร

```text

```

คุณยังทำอะไรด้วยตนเอง

```text

```

คุณคัดลอก code จากคนอื่นหรือไม่

```text
No
```

---

## 8. คำรับรองของนักศึกษา

เขียน `Yes` ในแต่ละ statement

| Statement | Yes/No |
|---|---|
| I wrote this submission in my own words. | Yes |
| I understand my final code. | Yes |
| I recorded the real OJ status. | Yes |
| I did not copy AI-generated text directly into this file. | Yes |
| I did not copy code from another person. | Yes |
| If I received human help, I disclosed it in this file. | Yes |
| I submitted the final code to the OJ by myself. | Yes |
