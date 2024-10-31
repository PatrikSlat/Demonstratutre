const express = require('express');
const app = express();
const PORT = process.env.PORT || 3000;
const axios = require('axios');

app.get("/vrijeme", async (req,res) => {
    try{
        const kljuc = "VAŠ KLJUČ"
        const url = `API_URL_ZA_POZIV + {kljuc}` /* Svaki API ima svoju dokumentaciju na kojoj možete pronaći URL + Ključ i sl.*/
        const upit = await axios.get(url) /* Uvijek await jer čekamo podatke*/
        console.log(upit)
    }catch(err){
        res.json({error: "Desila se greška"})
    }
})


app.listen(() => {
    console.log("Slušam na portu 3000")
})