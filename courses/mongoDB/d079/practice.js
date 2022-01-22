use myDB;
show collections;
db.persons.insertMany([{name: "victoria", age: 77},
    {name: 'sun', age: 77}, {name: "daniel", age: 34},
    {name: 'ammy', age: 21}, {name: "gracia", age: 24}]);
db.persons.drop()
db.persons.find()

const initData = [
    { "item": "journal", "qty": 25, "size": { "h": 14, "w": 21, "uom": "cm" }, "status": "A" },
    { "item": "notebook", "qty": 50, "size": { "h": 8.5, "w": 11, "uom": "in" }, "status": "A" },
    { "item": "paper", "qty": 100, "size": { "h": 8.5, "w": 11, "uom": "in" }, "status": "D" },
    { "item": "planner", "qty": 75, "size": { "h": 22.85, "w": 30, "uom": "cm" }, "status": "D" },
    { "item": "postcard", "qty": 45, "size": { "h": 10, "w": 15.25, "uom": "cm" }, "status": "A" }
]

db.inventory.insertMany(initData)
db.inventory.deleteMany(initData)
//practice1
db.inventory.find({qty:{$in:[50,75]}})
//practice2
db.inventory.find({status:{$nin:["A"]}})
//practice3
db.inventory.find({status:"D", qty:{$gt:80}})
//practice4
db.inventory.find({$or:[{qty:25},{qty:100}]})
//server path
db.serverCmdLineOpts()

// load("test.js")