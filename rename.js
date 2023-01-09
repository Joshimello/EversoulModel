// CH_%name%_WP_Base%random%.glb -> %name%.glb
// because windows made REN bad

const { join, extname, basename } = require('path')
const { readdirSync, renameSync } = require('fs')

let folder = './weapons'
for(let i of readdirSync(folder)){
    let ext = extname(i)
    let name = basename(i, ext)
    renameSync(join(folder, i), join(folder, name.split('_')[1].toLowerCase() + ext))
}