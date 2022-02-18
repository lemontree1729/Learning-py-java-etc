import { useState } from 'react'

function PhotoGallery() {
    const [photos, setPhotos] = useState<Array<string>>([])
    function addPhoto() {
        const photo = prompt("추가하려는 사진의 경로를 입력해주세요 !")
        setPhotos(photos => photo && !photos.includes(photo) ? [...photos, photo] : photos)
    }
    return (
        <>
            <button onClick={addPhoto}>add photo with url</button>
            <h1>Photo gallery</h1>
            ----------------------
            {photos.map(photo => <img src={photo} alt="photoimage" />)}
        </>
    )
}
export default PhotoGallery