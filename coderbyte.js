function camelCase(str) {
  return str.replace(/\W+(.)/g, function (_, chr) {
    // The regular expression /\W+(.)/g looks for one or more non-word characters (\W+)
    // followed by any character (.), and captures that character.
    return chr.toUpperCase();
    // For each match, this function returns the captured character (chr)
    // converted to uppercase
  });
}
console.log(camelCase("Bob loves coding"));
