from pytube import YouTube

def Download ( link ) :
	# Create a YouTube object by passing in the link
	youtubeObject = YouTube ( link )
	
	# Get the highest resolution stream from the YouTube object
	youtubeObject = youtubeObject.streams.get_highest_resolution ( )
	
	try :
		# Download the video
		youtubeObject.download ( )
	except :
		# If an error occurs, print an error message
		print ( 'There has been an error in downloading your youtube video' )
	# Print a completion message
	print ( 'This download has completed! Yahooooo!' )


# Get the link from the user
link = input ( 'Put your youtube link here!! URL:' )

# Download the video using the function
Download ( link )
