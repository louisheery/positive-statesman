

    < Link href = { article.url } >
        <GridListTileBar
            style={{ backgroundColor: 'white' }}

            title={<span>{article.title}</span>}
            titlePosition='top'
            rows={3}
            classes={{
                root: classes.otherTopArticleRoot,
                title: classes.otherTopArticleTitle,
            }}
        />
  </Link >

    <GridListTileBar
        style={{ backgroundColor: 'white' }}
        subtitle={<span><span style={{ float: 'left', display: 'inline-block', marginTop: '10px' }}>{article.publisher}</span><span style={{ float: 'right', marginTop: '10px' }}>{moment(`${article.publish_date}`).fromNow()}</span></span>}
        rows={3}
        classes={{
            root: classes.otherTopArticleSecondaryRoot,
            subtitle: classes.otherTopArticleSecondarySubtitle,
        }}
    />


    <GridListTileBar
        style={{ backgroundColor: 'white' }}
        className={classes.voteBar}
        titlePosition="bottom"
        title={
            <div className={classes.otherArticleTileVoteDiv}>
                <span style={{ float: 'left', display: 'inline-block' }}>

                    <ArticleVote articleId={article.id} />

                </span>
                <span style={{ float: 'right', display: 'inline-block' }}>

                    <Button className={classes.positivityScore} variant="outlined" color="primary" disableElevation disabled>
                        <span role="img" style={positivityTextStyle}>{positivityScorePcnt}%</span>
                    </Button>

                </span>
            </div>
        }
    />

