const express = require("express")
const words = require("./ag")

const app = express()
const PORT = 3000
app.use(express.urlencoded({ extended: true }))

function search(words, leg) {
    return words.find(word => word.name === leg.toUpperCase())
}

app.get("/",(req, res)=>{
    return res.send("hi guest")
})

app.post("/shop",(req, res)=>{
    const leg = req.body.leg

    if (leg == 'FLAG'){
        return res.status(403).send("Access Denied")
    }

    const obj = search(words,leg)

    if (obj){
        return res.send(JSON.stringify(obj))
    }
    
    return res.status(404).send("Nothing")
})

app.listen(PORT,()=>{
    console.log(`[+] Started on ${PORT}`)
})