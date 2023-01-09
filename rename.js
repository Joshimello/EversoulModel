// CH_%name%_WP_Base%random%.glb -> %name%.glb
// because windows made REN bad

const { join, extname, basename } = require('path')
const { readdirSync, renameSync, existsSync } = require('fs')

let folder = './weapons'

let list = readdirSync(folder)

console.log(list.length)

for(let i of list){
    let ext = extname(i)
    let name = basename(i, ext)

    let newname = name.split('_')[1].toLowerCase()

    let suffix = 0
    if(existsSync(join(folder, newname+String(suffix)+ext))){
        while(existsSync(join(folder, newname+String(suffix)+ext))){
            suffix++
        }
    }

    renameSync(join(folder, i), join(folder, newname+String(suffix)+ext))
}

// get folder stuff and craft into JSON

// const { join, extname, basename } = require('path')
// const { readdirSync, renameSync, writeFileSync } = require('fs')

// let folder = './weapons', list = {}
// for(let i of readdirSync(folder)){
//     let ext = extname(i)
//     let name = basename(i, ext)

//     list[name] = i
// }

// writeFileSync('./weapon_list.json', JSON.stringify(list, null, 4))