// get folder stuff and craft into JSON

const { join, extname, basename } = require('path')
const { readdirSync, renameSync, writeFileSync } = require('fs')

let folder = './weapons', list = {}
for(let i of readdirSync(folder)){
    let ext = extname(i)
    let name = basename(i, ext)

    list[name] = i
}

writeFileSync('./weapon_list.json', JSON.stringify(list, null, 4))