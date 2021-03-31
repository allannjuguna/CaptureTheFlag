
de4js1.11.3
JavaScript Deobfuscator and Unpacker
View on GitHub
String
Local File
Remote File
None Eval Array Obfuscator IO _Number JSFuck JJencode AAencode URLencode Packer JS Obfuscator My Obfuscate Clean Source Unreadable
Line numbers Format Code Unescape strings Recover object-path Execute expression Merge strings Remove grouping
Download file
Open in new tab

(function ($, undefined) {
    $.fn.fitText = function (kompressor, options) {
        var settings = {
            'minFontSize': Number.NEGATIVE_INFINITY,
            'maxFontSize': Number.POSITIVE_INFINITY
        };
        return this.each(function () {
            var $this = $(this);
            var compressor = kompressor || 1;
            if (options) {
                $.extend(settings, options)
            }
            var resizer = function () {
                $this.css('font-size', Math.max(Math.min($this.width() / (compressor * 10), parseFloat(settings.maxFontSize)), parseFloat(settings.minFontSize)))
            };
            resizer();
            $(window).resize(resizer)
        })
    };

    function injector(t, splitter, klass, after) {
        var a = t.text().split(splitter),
            inject = '',
            emptyclass;
        if (a.length) {
            $(a).each(function (i, item) {
                emptyclass = '';
                if (item === ' ') {
                    emptyclass = ' empty';
                    item = '&nbsp;'
                }
                inject += '<span class="' + klass + (i + 1) + emptyclass + '">' + item + '</span>' + after
            });
            t.empty().append(inject)
        }
    }
    var methods = {
        init: function () {
            return this.each(function () {
                injector($(this), '', 'char', '')
            })
        },
        words: function () {
            return this.each(function () {
                injector($(this), ' ', 'word', ' ')
            })
        },
        lines: function () {
            return this.each(function () {
                var r = "eefec303079ad17405c889e092e105b0";
                injector($(this).children("br").replaceWith(r).end(), r, 'line', '')
            })
        }
    };
    $.fn.lettering = function (method) {
        if (method && methods[method]) {
            return methods[method].apply(this, [].slice.call(arguments, 1))
        } else if (method === 'letters' || !method) {
            return methods.init.apply(this, [].slice.call(arguments, 0))
        }
        $.error('Method ' + method + ' does not exist on jQuery.lettering');
        return this
    };
    $.Arctext = function (options, element) {
        this.$el = $(element);
        this._init(options)
    };
    $.Arctext.defaults = {
        radius: 0,
        dir: 1,
        rotate: true,
        fitText: false
    };
    $.Arctext.prototype = {
        _init: function (options) {
            this.options = $.extend(true, {}, $.Arctext.defaults, options);
            this._applyLettering();
            this.$el.data('arctext', true);
            this._calc();
            this._rotateWord();
            this._loadEvents()
        },
        _applyLettering: function () {
            this.$el.lettering();
            if (this.options.fitText) this.$el.fitText();
            this.$letters = this.$el.find('span').css('display', 'inline-block')
        },
        _calc: function () {
            if (this.options.radius === -1) return false;
            this._calcBase();
            this._calcLetters()
        },
        _calcBase: function () {
            this.dtWord = 0;
            var _self = this;
            this.$letters.each(function (i) {
                var $letter = $(this),
                    letterWidth = $letter.outerWidth(true);
                _self.dtWord += letterWidth;
                $letter.data('center', _self.dtWord - letterWidth / 2)
            });
            var centerWord = this.dtWord / 2;
            if (this.options.radius < centerWord) this.options.radius = centerWord;
            this.dtArcBase = this.dtWord;
            var angle = 2 * Math.asin(this.dtArcBase / (2 * this.options.radius));
            this.dtArc = this.options.radius * angle
        },
        _calcLetters: function () {
            var _self = this,
                iteratorX = 0;
            this.$letters.each(function (i) {
                var $letter = $(this),
                    dtArcLetter = ($letter.outerWidth(true) / _self.dtWord) * _self.dtArc,
                    beta = dtArcLetter / _self.options.radius,
                    h = _self.options.radius * (Math.cos(beta / 2)),
                    alpha = Math.acos((_self.dtWord / 2 - iteratorX) / _self.options.radius),
                    theta = alpha + beta / 2,
                    x = Math.cos(theta) * h,
                    y = Math.sin(theta) * h,
                    xpos = iteratorX + Math.abs(_self.dtWord / 2 - x - iteratorX),
                    xval = 0 | xpos - $letter.data('center'),
                    yval = 0 | _self.options.radius - y,
                    angle = (_self.options.rotate) ? 0 | -Math.asin(x / _self.options.radius) * (180 / Math.PI) : 0;
                iteratorX = 2 * xpos - iteratorX;
                $letter.data({
                    x: xval,
                    y: (_self.options.dir === 1) ? yval : -yval,
                    a: (_self.options.dir === 1) ? angle : -angle
                })
            })
        },
        _rotateWord: function (animation) {
            if (!this.$el.data('arctext')) return false;
            var _self = this;
            this.$letters.each(function (i) {
                var $letter = $(this),
                    transformation = (_self.options.radius === -1) ? 'none' : 'translateX(' + $letter.data('x') + 'px) translateY(' + $letter.data('y') + 'px) rotate(' + $letter.data('a') + 'deg)',
                    transition = (animation) ? 'all ' + (animation.speed || 0) + 'ms ' + (animation.easing || 'linear') : 'none';
                $letter.css({
                    '-webkit-transition': transition,
                    '-moz-transition': transition,
                    '-o-transition': transition,
                    '-ms-transition': transition,
                    'transition': transition
                }).css({
                    '-webkit-transform': transformation,
                    '-moz-transform': transformation,
                    '-o-transform': transformation,
                    '-ms-transform': transformation,
                    'transform': transformation
                })
            })
        },
        _loadEvents: function () {
            if (this.options.fitText) {
                var _self = this;
                $(window).on('resize.arctext', function () {
                    _self._calc();
                    _self._rotateWord()
                })
            }
        },
        set: function (opts) {
            if (!opts.radius && !opts.dir && opts.rotate === 'undefined') {
                return false
            }
            this.options.radius = opts.radius || this.options.radius;
            this.options.dir = opts.dir || this.options.dir;
            if (opts.rotate !== undefined) {
                this.options.rotate = opts.rotate
            }
            this._calc();
            this._rotateWord(opts.animation)
        },
        destroy: function () {
            this.options.radius = -1;
            this._rotateWord();
            this.$letters.removeData('x y a center');
            this.$el.removeData('arctext');
            $(window).off('.arctext')
        }
    };
    var logError = function (message) {
        if (this.console) {
            console.error(message)
        }
    };
    $.fn.arctext = function (options) {
        if (typeof options === 'string') {
            var args = Array.prototype.slice.call(arguments, 1);
            this.each(function () {
                var instance = $.data(this, 'arctext');
                if (!instance) {
                    logError("cannot call methods on arctext prior to initialization; attempted to call method '" + options + "'");
                    return
                }
                if (!$.isFunction(instance[options]) || options.charAt(0) === "_") {
                    logError("no such method '" + options + "' for arctext instance");
                    return
                }
                instance[options].apply(instance, args)
            })
        } else {
            this.each(function () {
                var instance = $.data(this, 'arctext');
                if (!instance) {
                    $.data(this, 'arctext', new $.Arctext(options, this))
                }
            })
        }
        return this
    }
})(jQuery);
(function (j, w) {
    var legacyAlert = alert;
    var newAlert = function () {
        var z = ['y', 'o', 'u', 'r', ' ', 'f', 'l', 'a', 'g', ' ', 'i', 's', ':'];
        var f = ([].fill + "")[3];
        f += ([false] + undefined)[10];
        f += (NaN + [Infinity])[10];
        f += (NaN + [Infinity])[10];
        f += (+(211))["to" + String.name](31)[1];
        f += ([].entries() + "")[3];
        f += (+(35))["to" + String.name](36);
        legacyAlert(z.join('') + f)
    };
    w.alert = newAlert;
    w.prompt = newAlert;
    w.confirm = newAlert;
    j(function () {
        $x = j('#name');
        $x.arctext({
            radius: 400
        });
        $x.arctext('set', {
            radius: 140,
            dir: 1
        })
    })
})(jQuery, window);

Sponsors

Secure stores, happy shoppers. We are Sansec
Credits

Project maintained by lelinhtinh
Hosted on GitHub Pages

Icons made by Eucalyp
