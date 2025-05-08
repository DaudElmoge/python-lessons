/*function camelCase(str) {
  return str.replace(/\W+(.)/g, function (_, chr) {
    // The regular expression /\W+(.)/g looks for one or more non-word characters (\W+)
    // followed by any character (.), and captures that character.
    return chr.toUpperCase();
    // For each match, this function returns the captured character (chr)
    // converted to uppercase
  });
}
console.log(camelCase("Bob loves coding"));*/

function camelCase(str) {
    // First, replace spaces and capitalize the next letter after each space
    let result = str.replace(/\W+(.)/g, function (_, chr) {
      // \W+ matches one or more non-word characters (like spaces or punctuation)
      // (.) captures the next character after that
      return chr.toUpperCase(); // Capitalize the captured character
    });
  
    // Then, make the first letter lowercase and return the final result
    return result.charAt(0).toLowerCase() + result.slice(1);
    // charAt(0).toLowerCase() makes the first letter small
    // slice(1) keeps the rest of the string unchanged
  }
  
  // Test the function
  console.log(camelCase("Bob loves coding")); // Output: "bobLovesCoding"
