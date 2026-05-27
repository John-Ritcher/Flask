/*const story = document.querySelector('.story');

const setText = document.querySelector('#set-text');
setText.addEventListener('click', () => {
    story.textContent = 'It was a dark night and stormy night';
})

const clearText = document.querySelector('#clear-text');
clearText.addEventListener('click', () => {
    story.textContent = '';
})*/

/*const parent = document.querySelector('.parent');

const addChild = document.querySelector('#add-child');
addChild.addEventListener('click', () => {
    // Only add a child if we don't already have one, in addition to the text node "parent"
    if (parent.childNodes.length > 1) {
        return;
    }
    const child = document.createElement("div");
    child.classList.add("child");
    child.textContent = "child";
    parent.appendChild(child);
})

const removeChild = document.querySelector('#remove-child');
removeChild.addEventListener('click', () => {
    const child = document.querySelector('.child');
    parent.removeChild(child);
})

function stopEvent(event) {
    const c2 = document.getElementById("c2");
    c2.textContent = "Hello World!";

    event.stopPropagation();
    console.log("event propagation halted.");
}

const elem = document.getElementById("tbl1");
elem.addEventListener("click", stopEvent);

document.getElementById("t-dad").addEventListener("click", () => {
    console.log("t-dad clicked");
});*/


const tabs = document.querySelectorAll(".changeImg li");
const tabs2 = document.querySelectorAll(".changeImg2 li");
const myImage1 = document.querySelector("#JH");
const myImage2 = document.querySelector('#CH');
//const myImage = document.querySelectorAll('img');
//console.log(myImage);

tabs.forEach(tab => {
    tab.addEventListener("click", () => {
        const mySrc = myImage1.getAttribute("src");
        tabs.forEach( t => t.classList.remove("active"))
            if (!tab.classList.contains("active"))
                {
                    tab.classList.add("active");
                }
        if (tab.textContent === "Masked")
        {
            if (mySrc !== "../static/imgs/Jungle_Predator.jpeg")
            {
                myImage1.setAttribute("src", "../static/imgs/Jungle_Predator.jpeg");
                tab.classList.add("active");
            }
        }
        else if (tab.textContent === "Unmasked")
        {
            if (mySrc !== "../static/imgs/Jungle_Hunter_Unmasked.jpeg")
            {
                myImage1.setAttribute("src", "../static/imgs/Jungle_Hunter_Unmasked.jpeg");
                tab.classList.add("active");
            }
        }
    })
})

tabs2.forEach(tab => {
    tab.addEventListener("click", () => {
        /*myImage.forEach(i => {
            const mySrc = i.getAttribute("src")

        });*/
        const mySrc2 = myImage2.getAttribute("src")
        console.log("Teste");
        tabs2.forEach( t => t.classList.remove("active"))
            if (!tab.classList.contains("active"))
                {
                    tab.classList.add("active");
                };
        if (tab.textContent === "Masked")
        {
            if (mySrc2 !== "../static/imgs/City_Hunter_Masked.jpeg")
            {
                myImage2.setAttribute("src", "../static/imgs/City_Hunter_Masked.jpeg");
                tab.classList.add("active");
            }
        }
        else if (tab.textContent === "Unmasked")
        {
            if (mySrc2 !== "../static/imgs/City_Hunter_Unmasked.jpeg")
            {
                myImage2.setAttribute("src", "../static/imgs/City_Hunter_Unmasked.jpeg");
                tab.classList.add("active");
            }
        }
    })
})

const tables = document.getElementsByTagName("ul");
const firstTable = tables.item(1); // or tables[1] - returns the second table in the DOM
console.log(firstTable);