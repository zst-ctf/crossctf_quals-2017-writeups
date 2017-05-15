#! /usr/bin/ruby
require 'chunky_png'
 
image1 = ChunkyPNG::Image.from_file(ARGV[0])
keyR = ARGV[1]
keyG = ARGV[2]
keyB = ARGV[3]
 
def go(r,g,b,image)
        range=2
        if r.to_i>255 or r.to_i<0 or g.to_i>255 or g.to_i<0 or b.to_i>255 or b.to_i<0
                puts "Invalid arguments. Syntax is ./findColorin [IMAGE] [R VALUE] [G VALUE] [B VALUE]"
                return 0
        end
        (0..image.dimension.width-1).each do |x|
                (0..image.dimension.height-1).each do |y|
                        if (image[x,y] > ChunkyPNG::Color.rgb(r.to_i-range,g.to_i-range,b.to_i-range))and(image[x,y] < ChunkyPNG::Color.rgb(r.to_i+range,g.to_i+range,b.to_i+range))
                                image[x,y] = ChunkyPNG::Color.rgb(0,0,0)
                        else
                                image[x,y] = ChunkyPNG::Color.rgb(255,255,255)
                        end
                end
        end    
        puts "Saving to output.png"
        image.save('output.png')
end
 
go keyR, keyG, keyB, image1