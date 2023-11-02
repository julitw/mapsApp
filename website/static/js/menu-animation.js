const imageDivs = document.querySelectorAll('.menu_item');
const imageDivsM = document.querySelectorAll('.menu_item--main');
console.log(imageDivsM)
const imageDivsH = document.querySelectorAll('.menu_item--hidden');

const titles= document.querySelectorAll('.menu_item__title');

// imageDivsM[0].style.backgroundImage =  "url({{ url_for ('static', filename = 'images/menu_item_1/fire.jpg') }})"
imageDivsM[0].style.backgroundImage =  "url({{ url_for ('static', filename = 'images/menu_item_3/imageonline/00.jpg') }})"
imageDivsM[1].style.backgroundImage =  "url({{ url_for ('static', filename = 'images/menu_item_2/imageonline/10.jpg') }})"
imageDivsM[2].style.backgroundImage =  "url({{ url_for ('static', filename = 'images/menu_item_1/imageonline/20.jpg') }})"
imageDivsM[3].style.backgroundImage =  "url({{ url_for ('static', filename = 'images/menu_item_4/imageonline/30.jpg') }})"



imageDivs.forEach(imageDiv => {
    console.log('forech')
    imageDiv.addEventListener('mouseover', ()=>{
        lines.forEach(line => {
            line.style.display = 'block'
        })
        const index = imageDiv.getAttribute('data-index');
        if(index == 0){
            imageDivsH[1].style.left = '0'
            imageDivsH[2].style.left = '0'
            imageDivsH[3].style.left = '0'
            imageDivsH[0].style.backgroundImage =  "url({{ url_for ('static', filename = 'images/menu_item_3/imageonline/00.jpg') }})"
            imageDivsH[1].style.backgroundImage = "url({{ url_for ('static', filename = 'images/menu_item_3/imageonline/10.jpg') }})"
            imageDivsH[2].style.backgroundImage = "url({{ url_for ('static', filename = 'images/menu_item_3/imageonline/20.jpg') }})"
            imageDivsH[3].style.backgroundImage = "url({{ url_for ('static', filename = 'images/menu_item_3/imageonline/30.jpg') }})"
            titles[0].style.display = 'block'
            titles[1].style.display = 'none'
            titles[2].style.display = 'none'
            titles[3].style.display = 'none'
        }
        else if(index == 1){
            imageDivsH[0].style.backgroundImage =  "url({{ url_for ('static', filename = 'images/menu_item_2/imageonline/00.jpg') }})"
            imageDivsH[1].style.backgroundImage = "url({{ url_for ('static', filename = 'images/menu_item_2/imageonline/10.jpg') }})"
            imageDivsH[2].style.backgroundImage = "url({{ url_for ('static', filename = 'images/menu_item_2/imageonline/20.jpg') }})"
            imageDivsH[3].style.backgroundImage = "url({{ url_for ('static', filename = 'images/menu_item_2/imageonline/30.jpg') }})"
            titles[0].style.display = 'none'
            titles[1].style.display = 'block'
            titles[2].style.display = 'none'
            titles[3].style.display = 'none'
            imageDivsH[0].style.left = '0'
            imageDivsH[2].style.left = '0'
            imageDivsH[3].style.left = '0'
        }
        else if(index == 2){
            imageDivsH[0].style.backgroundImage =  "url({{ url_for ('static', filename = 'images/menu_item_1/imageonline/00.jpg') }})"
            imageDivsH[1].style.backgroundImage = "url({{ url_for ('static', filename = 'images/menu_item_1/imageonline/10.jpg') }})"
            imageDivsH[2].style.backgroundImage = "url({{ url_for ('static', filename = 'images/menu_item_1/imageonline/20.jpg') }})"
            imageDivsH[3].style.backgroundImage = "url({{ url_for ('static', filename = 'images/menu_item_1/imageonline/30.jpg') }})"
            titles[0].style.display = 'none'
            titles[1].style.display = 'none'
            titles[2].style.display = 'block'
            titles[3].style.display = 'none'
            imageDivsH[0].style.left = '0'
            imageDivsH[1].style.left = '0'
            imageDivsH[3].style.left = '0'
        }
        else if(index == 3){
            imageDivsH[0].style.backgroundImage =  "url({{ url_for ('static', filename = 'images/menu_item_3/imageonline/00.jpg') }})"
            imageDivsH[1].style.backgroundImage = "url({{ url_for ('static', filename = 'images/menu_item_3/imageonline/10.jpg') }})"
            imageDivsH[2].style.backgroundImage = "url({{ url_for ('static', filename = 'images/menu_item_3/imageonline/20.jpg') }})"
            imageDivsH[3].style.backgroundImage = "url({{ url_for ('static', filename = 'images/menu_item_3/imageonline/30.jpg') }})"
            titles[0].style.display = 'none'
            titles[1].style.display = 'none'
            titles[2].style.display = 'none'
            titles[3].style.display = 'block'
            imageDivsH[0].style.left = '0'
            imageDivsH[1].style.left = '0'
            imageDivsH[2].style.left = '0'
        }
        // imageDivsH.forEach(imageDivH =>{
        //     imageDivH.style.left = '0'
        // })
})})

imageDivs.forEach(imageDiv => {
    imageDiv.addEventListener('mouseout', ()=>{
    imageDivsH.forEach(imageDivH =>{
        imageDivH.style.left = '-100%'
    })

    lines.forEach(line => {
            line.style.display = 'none'
        })
    titles[0].style.display = 'block'
    titles[1].style.display = 'block'
    titles[2].style.display = 'block'
    titles[3].style.display = 'block'
})})



imageDivs[0].addEventListener("click", function() {
        // Przenieś użytkownika na wskazaną stronę (np. 'map1')
        window.location.href = "{{ url_for('map1.map1') }}";
});

imageDivs[1].addEventListener("click", function() {
        // Przenieś użytkownika na wskazaną stronę (np. 'map1')
        window.location.href = "{{ url_for('map1.map1') }}";
});

imageDivs[2].addEventListener("click", function() {
        // Przenieś użytkownika na wskazaną stronę (np. 'map1')
        window.location.href = "{{ url_for('map1.map1') }}";
});

imageDivs[3].addEventListener("click", function() {
        // Przenieś użytkownika na wskazaną stronę (np. 'map1')
        window.location.href = "{{ url_for('map1.map1') }}";
});