const ComicList = (props) => {
    return (
        <div className="mt-2">
            {props.comics && props.comics.map(comic => {
                return (
                    <div key={comic.title}>
                        <h2 className="text-primary"> {comic.title} </h2>
                    </div>
                )
            })}
        </div>
    )
}

export default ComicList;