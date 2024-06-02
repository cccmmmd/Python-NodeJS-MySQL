const mysql= require("mysql2/promise");

async function connectDatabase(){

    const con=await mysql.createConnection({
        user: "root",
        password: "1234567",
        host: "localhost",
        database: "mydb"
    });
    //  新增資料
    let [results] = await con.execute("INSERT INTO product(name) VALUES('綠茶')");
    console.log(results);

    // 刪除資料
    let [results2] = await con.execute('DELETE FROM product WHERE id=14');


    // 修改資料
    let [results3] = await con.execute("UPDATE product SET name='美式咖啡' WHERE id=2");

    // 修改資料，帶入變數
    let productName = '西西里咖啡';
    let productId = 1;

    let [results5] = await con.execute("UPDATE product SET name=? WHERE id=?", [productName, productId]);


    // 查找資料
    let [result4] = await con.execute("SELECT * FROM product")
    result4.forEach((pd) => {
        console.log(pd.name)
    })
    //  關閉連線
    con.end();
}

connectDatabase();