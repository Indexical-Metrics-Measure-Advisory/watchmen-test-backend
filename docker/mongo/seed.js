db.createUser(
    {
        user:"watchmen",
        pwd:"watchmen-pwd",
        roles:[
            {
                role: "readWrite",
                db :"watchmen"

            }
        ]
    }
)