# MenuToday
PSCP Project
## Setup
Cloning the repository
	
	git clone https://github.com/NitruZx/MenuToday.git

Install Flask framework

	pip install Flask
## Running the app
 In folder MenuToday
 - python Main_app
## รายละเอียดการทำโปรเจกต์
- โปรเจกต์นี้ทำเกี่ยวกับการเลือกเมนูอาหารที่สอดคล้องกับปริมาณแคลลอรี่ โดยใช้ภาษา Python ในการเขียน หลังจากที่ได้หัวข้อโปรเจกต์ พวกเราได้ออกแบบการทำงานของโปรแกรม โดยเริ่มจากการออกแบบ Flow chart จากนั้นจึงเริ่มเขียนโค้ดในภาษา Python เมื่อส่วนของการทำงานภายในโปรแกรมเสร็จแล้ว พวกเราจึงเริ่มออกแบบหน้าต่างของเว็บ รวมถึงศึกษาวิธีการเขียนเว็บ
Link Youtube presentation : https://www.youtube.com/watch?v=ZT3awDJIkZM
Link GitHub Repository : https://github.com/NitruZx/MenuToday
## อุปสรรคระหว่างการทำโปรเจกต์
- มีอุปสรรคในการทำคือพวกเราต้องศึกษาวิธีการเขียนเว็บ เนื่องจากพวกเราไม่เคยทำในส่วนนี้มาก่อน เพื่อให้เว็บมีการแสดงผลตรงตามที่เราได้ออกแบบไว้ และมีปัญหาในการเขียนโค้ดบางการคำนวณที่ไม่ได้ผลลัพธ์ตามที่ต้องการ พวกเราจึงแก้ไขโดยการศึกษาข้อมูลเพิ่มเติมหรือสอบถามเพื่อนที่ทราบในส่วนนี้
## ประโยชน์ของโปรเจกต์
- ช่วยแนะนำเมนูอาหาร พร้อมกับบอกปริมาณแคลลอรี่ที่ผู้ใช้ต้องการในหนึ่งวัน และปริมาณแคลลอรี่ของเมนูอาหารที่แนะนำ
## การทำงานของระบบ
  Input ครั้งที่ 1 : จะมีการรับค่าอายุ น้ำหนัก ส่วนสูง และเพศของผู้ใช้ จากนั้นจะนำข้อมูลไปคำนวณค่า BMI และ BMR(ปริมาณแคลลอรี่ที่เหมาะสมแต่ละช่วงวัยและเพศ) แล้วจะ Output ค่า BMI และ BMR ที่คำนวณได้
	
  Input ครั้งที่ 2 : จะมีการรับค่าแคลลอรี่ที่ผู้ใช้ต้องการในหนึ่งวัน โดยจะใช้ตามที่เว็บแนะนำ หรือจะกำหนดขึ้นมาใหม่ก็ได้ มีการรับข้อมูลจำนวนมื้ออาหารที่ต้องการ และประเภทของอาหาร(ข้าว, เส้น, ยำ) เว็บจะคำนวณแคลลอรี่ต่อมื้อ โดยการนำแคลลอรี่ที่ผู้ใช้ต้องการหารด้วยจำนวนมื้อที่ต้องการ เมื่อได้แคลลอรี่ต้องมื้อแล้วเว็บนำแคลลอรี่ที่ได้ไปสุ่มเมนูอาหารตามประเภทอาหารที่ผู้ใช้เลือก จากนั้นจะ Output เมนูอาหารตามจำนวนมื้อที่สุ่มได้พร้อมกับแคลลอรี่ของอาหารนั้น ๆ และแคลลอรี่รวมของทุกเมนู
## - บทบาทของสมาชิก -
65070003 นายกณิศพงศ์ ศรีเจริญ : ออกแบบ flowchart เขียนโค้ดภายในโปรแกรมโดยใช้ภาษา Python (Main)

65070041 นายเจษฎา แต่งสุวรรณ์ : หาข้อมูลวิธีการเขียนเว็บ เขียนโค้ดเว็บไซต์โดยใช้ภาษา html, CSS, jinja

65070082 น.ส.ณัฐรดา กิจสมบูรณ์สุข : หาข้อมูลที่ใช้ในโปรแกรม เช่น เมนูอาหาร Calories เขียนโค้ดภายในโปรแกรมโดยใช้ภาษา Python (Support), ทำรายงาน
## เอกสารอ้างอิง
https://www.youtube.com/watch?v=USjZcfj8yxE&t=195s
https://www.youtube.com/watch?v=RR_Ih6d71YA&t=1579s
https://www.youtube.com/watch?v=U1JUicQzGMI&t=5349s
https://www.youtube.com/watch?v=dam0GPOAvVI&t=3565s
https://www.w3schools.com/python/
https://hd.co.th/table-of-calories-in-food-types
https://www.lovefitt.com/เครื่องคำนวณหาค่าดัชนีมวลกาย-bmi/
