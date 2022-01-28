show dbs;

use myDB;

use test;

db.dropDatabase()

db.restaurant.insertMany([
    {"_id": 1, "name": "Central Perk Cafe", "Borough": "Manhattan"},
    {"_id": 2, "name": "Rock A Feller Bar and Grill", "Borough": "Queens", "violations": 2},
    {"_id": 3, "name": "Empire State Pub", "Borough": "Brooklyn", "violations": 0}
])

show collections;

db.restaurant.find().pretty()

db.restaurant.updateOne({"name": "Central Perk Cafe"}, {$set: {"violations": 3}})

db.products.insertOne(
    {
        _id: 100,
        quantity: 250,
        instock: true,
        reorder: false,
        details: {model: "14QQ", make: "Clothes Corp"},
        tags: ["apparel", "clothing"],
        ratings: [{by: "Customer007", rating: 4}]
    }
)

db.products.updateOne(
    {_id: 100},
    {
        $set:
            {
                quantity: 500,
                details: {model: "2600", make: "Fashionaires"},
                tags: ["coats", "outerwear", "clothing"]
            }
    }
)
db.products.find().pretty()

db.products.updateOne(
    {_id: 100},
    {$set: {"details.make": "Kustom Kidz"}}
)

db.products.updateOne(
    {_id: 100},
    {
        $set:
            {
                "tags.1": "rain gear",
                "ratings.0.rating": 2
            }
    }
)

db.members.insertMany([
    {
        "_id": 1,
        "member": "abc123",
        "status": "A",
        "points": 2,
        "misc1": "note to self: confirm status",
        "misc2": "Need to activate",
        "lastUpdate": ISODate("2019-01-01T00:00:00Z")
    },
    {
        "_id": 2,
        "member": "xyz123",
        "status": "A",
        "points": 60,
        comments: ["reminder: ping me at 100pts", "Some random comment"],
        "lastUpdate": ISODate("2019-01-01T00:00:00Z")
    }
])

db.members.find()

db.members.updateOne(
    {_id: 1},
    [
        {$set: {status: "Modified", comments: ["$misc1", "$misc2"], lastUpdate: "$$NOW"}},
        {$unset: ["misc1", "misc2"]}
    ]
)

db.students.insertOne({_id: 1, scores: [44, 78, 38, 80]})

db.students.find()

db.students.updateOne(
    {_id: 1},
    {$push: {scores: 89}}
)

db.students.updateOne(
    {_id: 1},
    {$push: {scores: {$each: [90, 92, 95]}}}
)

db.students.updateOne(
    {_id: 1},
    {$addToSet: {scores: {$each: [90, 92, 95]}}}
)

db.students.updateOne(
    {_id: 1},
    {
        $push: {
            scores: {
                $each: [2, 124, 49],
                $sort: -1,
                $slice: 5
            }
        }
    }
)

db.students.updateOne(
    {_id: 1},
    {$pop: {scores: 1}}
)