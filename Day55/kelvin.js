/* Simple script to calculate temperature in Fahrenheit and Newton
based on Kelvin as Input

*/
//kelvin represents the forecast of todays tempreature
kelvin = 0
//celsius is 273 degrees less than kelvin
celsius = kelvin-273
//fahrenheit = Celsius*(9/5)+32
fahrenheit = Math.floor(celsius*(9/5)+32)
console.log(`The temperature is ${fahrenheit} degrees Fahrenheit.`)
newton = celsius*(33/100)
newton = Math.floor(newton)
console.log(`The temperature is ${newton} degrees Newton.`)