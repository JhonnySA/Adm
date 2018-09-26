(function ($) {
  var init = function ($element, options) {
    $element.select2(options)
  };

  var initHeavy = function ($element, options) {
    $dependentFields0 = $element.data('select2-dependent-fields');
    if ($dependentFields0 != undefined) {
        $dependentFields0 = $dependentFields0.trim().split(/\s+/);
        $.each($dependentFields0, function (i, dependentField) {
          // objdep = $('#' + dependentField);
          // if (!objdep) objdep = $('[name="' + dependentField + '"]');
          objdep = $('[name="' + dependentField + '"]');
          objdep.on("change", function() {
            $element.val("").trigger("change");
          });
        });
    }
    var settings = $.extend({
        // quietMillis: 1000,
      dropdownParent: $element.parent() || null,
      ajax: {
        delay: 1000,
        data: function (params) {
          var result = {
            term: params.term,
            page: params.page,
            field_id: $element.data('field_id')
          };
          $dependentFields = $element.data('select2-dependent-fields');
          if ($dependentFields != undefined) {
            $dependentFields = $dependentFields.trim().split(/\s+/);
            $.each($dependentFields, function (i, dependentField) {
              // objdep = $('#' + dependentField);
              // if (!objdep) objdep = $('[name="' + dependentField + '"]');
              objdep = $('select[name="' + dependentField + '"]');
              valdep = objdep.val();
              if (!valdep) valdep = 0;
              result[dependentField] = valdep;
            })
          }
          return result
        },
        processResults: function (data, page) {
          return {
            results: data.results,
            pagination: {
              more: data.more
            }
          }
        }
      }
    }, options);

    $element.select2(settings);
  };

  $.fn.select2.defaults.set('language', 'es');
  $.fn.select2.defaults.set('width', '100%');

  $.fn.djangoSelect2 = function (options) {
    var settings = $.extend({}, options);
    $.each(this, function (i, element) {
      var $element = $(element);
      if ($element.hasClass('django-select2-heavy')) {
        initHeavy($element, settings)
      } else {
        init($element, settings)
      }
    });
    return this
  };

  $(function () {
    $('.django-select2').djangoSelect2();
  })
}(this.jQuery));

