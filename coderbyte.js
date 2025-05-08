function camelCase(str) {
    return str.replace(/\W+(.)/g, function (_,chr) {
        return chr.toUpperCase()
    });
}
console.log(camelCase("Bob loves coding"))