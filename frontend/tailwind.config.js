/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./src/**/*.{js,jsx,ts,tsx}"

  ],
  theme: {
   
    extend: {
      colors:{
        'ui-grey': '#2a2d34',
      },
      screens: {
        '3xl': '1600px',
        '4xl': '1920px',
      },
    },
  },
  plugins: [

  ],
}
