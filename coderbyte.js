function camelCase(str) {
    return str.replace(/\W+(.)/g, function (match,chr) {
        return chr.toUpperCase()
    });
}
console.log(camelCase("Bob loves coding"))